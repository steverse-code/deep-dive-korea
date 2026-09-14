#!/usr/bin/env python3
"""
publish.py — 카드뉴스 캐러셀을 Instagram에 발행한다.

Instagram API with Instagram Login (Facebook 페이지 불필요)
  base: https://graph.instagram.com/v24.0

필요한 환경변수
  IG_USER_ID        Instagram 프로페셔널 계정 ID
  IG_ACCESS_TOKEN   장기 액세스 토큰 (60일, refresh_token.py로 자동 갱신)
  IMAGE_BASE_URL    슬라이드 이미지가 공개 서빙되는 베이스 URL
                    예) https://raw.githubusercontent.com/<user>/<repo>/main

사용
  python3 scripts/publish.py              # 오늘 발행할 최신 글 1건만 발행
  python3 scripts/publish.py --dry-run    # 실제 발행 없이 점검만
  python3 scripts/publish.py --slug 2026-08-17-vo2max   # 특정 글 강제 발행
  python3 scripts/publish.py --slug 2026-08-17-vo2max --reel   # 같은 글을 릴스(mp4)로 발행
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

API = "https://graph.instagram.com/v24.0"
KST = timezone(timedelta(hours=9))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "queue.json")

MAX_CAPTION = 2200
MAX_HASHTAGS = 8
MAX_SLIDES = 10          # 인스타 캐러셀 상한
MIN_SLIDES = 2

DEFAULT_MAX_PER_RUN = 1


# ─────────────────────────────────────────────────────────────
def _req(method: str, url: str, data: dict | None = None) -> dict:
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {url.split('?')[0]} → HTTP {e.code}\n{detail}") from None


def get(path: str, **params) -> dict:
    return _req("GET", f"{API}{path}?{urllib.parse.urlencode(params)}")


def post(path: str, **data) -> dict:
    return _req("POST", f"{API}{path}", data)


# ─────────────────────────────────────────────────────────────
def build_caption(spec: dict) -> str:
    tags = spec.get("hashtags", [])
    limit = MAX_HASHTAGS if int(spec.get("policy_version", 1)) >= 2 else 30
    if len(tags) > limit:
        raise ValueError(f"해시태그 {len(tags)}개 — 운영 상한은 {limit}개입니다.")
    caption = spec["caption"].rstrip()
    if tags:
        caption += "\n\n" + " ".join(tags)
    if len(caption) > MAX_CAPTION:
        raise ValueError(f"캡션 {len(caption)}자 — 상한 {MAX_CAPTION}자를 넘습니다.")
    return caption


def validate_rights(spec: dict) -> None:
    """새 정책(v2+) 콘텐츠는 출처와 사용권 확인 없이는 발행하지 않는다."""
    if int(spec.get("policy_version", 1)) < 2:
        print("  ! 레거시 콘텐츠: 신규 미디어 권리 메타데이터 검사를 생략합니다")
        return
    source = spec.get("asset_source")
    allowed = {"original", "partner_licensed", "licensed_stock"}
    if source not in allowed or spec.get("rights_confirmed") is not True:
        raise ValueError(
            "미디어 권리 확인 실패 — asset_source와 rights_confirmed=true가 필요합니다."
        )
    if spec.get("collab_required") and spec.get("collab_status") != "accepted":
        raise ValueError("Collab 게시물은 파트너 수락 확인 후에만 발행할 수 있습니다.")


def slide_urls(spec: dict, base: str) -> list[str]:
    n = len(spec["slides"])
    if not (MIN_SLIDES <= n <= MAX_SLIDES):
        raise ValueError(f"슬라이드 {n}장 — 캐러셀은 {MIN_SLIDES}~{MAX_SLIDES}장이어야 합니다.")
    base = base.rstrip("/")
    return [f"{base}/out/{spec['slug']}/{spec['slug']}_{i+1:02d}.jpg" for i in range(n)]


def check_reachable(urls: list[str], expect: tuple[str, ...] | None = ("jpeg", "jpg")) -> None:
    """인스타그램은 공개 URL에서 미디어를 가져간다. 미리 확인.

    GitHub raw는 mp4에 Content-Type을 application/octet-stream으로 내려줘서
    (jpeg와 달리) 타입 검증이 무의미하다 — expect=None이면 200 응답만 확인한다.
    """
    for u in urls:
        req = urllib.request.Request(u, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if expect is None:
                    continue
                ct = r.headers.get("Content-Type", "")
                if not any(e in ct for e in expect):
                    raise RuntimeError(f"{'/'.join(expect)}가 아닙니다 ({ct}): {u}")
        except Exception as e:
            raise RuntimeError(f"미디어에 접근할 수 없습니다: {u}\n  {e}") from None


def wait_ready(container_id: str, token: str, tries: int = 30, delay: int = 5) -> None:
    """컨테이너가 FINISHED 될 때까지 대기."""
    for _ in range(tries):
        st = get(f"/{container_id}", fields="status_code,status", access_token=token)
        code = st.get("status_code")
        if code == "FINISHED":
            return
        if code == "ERROR":
            raise RuntimeError(f"컨테이너 처리 실패: {st}")
        time.sleep(delay)
    raise RuntimeError(f"컨테이너 {container_id} 준비 시간 초과")


# ─────────────────────────────────────────────────────────────
def publish(spec: dict, ig_id: str, token: str, base_url: str, dry: bool = False) -> str | None:
    caption = build_caption(spec)
    urls = slide_urls(spec, base_url)

    print(f"▸ {spec['slug']} · 슬라이드 {len(urls)}장 · 캡션 {len(caption)}자")
    check_reachable(urls)
    print("  이미지 접근 확인 완료")

    if dry:
        print("  [dry-run] 여기서 중단합니다.")
        for u in urls:
            print("   ", u)
        return None

    children = []
    for i, u in enumerate(urls, 1):
        r = post(f"/{ig_id}/media", image_url=u, is_carousel_item="true", access_token=token)
        children.append(r["id"])
        print(f"  슬라이드 {i}/{len(urls)} 업로드 → {r['id']}")

    for cid in children:
        wait_ready(cid, token)

    carousel = post(f"/{ig_id}/media",
                    media_type="CAROUSEL",
                    children=",".join(children),
                    caption=caption,
                    access_token=token)
    print(f"  캐러셀 컨테이너 {carousel['id']}")
    wait_ready(carousel["id"], token)

    published = post(f"/{ig_id}/media_publish", creation_id=carousel["id"], access_token=token)
    media_id = published["id"]

    info = get(f"/{media_id}", fields="permalink,timestamp", access_token=token)
    print(f"✅ 발행 완료 → {info.get('permalink')}")
    return media_id


# ─────────────────────────────────────────────────────────────
# 릴스 오디오 페이지에 표시될 이름 — 필러별로 한 줄
AUDIO_NAME = {
    "longevity": "롱제비티 — 근거로 뒷받침되는 선택지",
    "aging_news": "노화·의학 뉴스 — 근거로 뒷받침되는 선택지",
    "ai_news": "AI 소식 — 근거로 뒷받침되는 선택지",
    "food": "한국 맛집 — 근거로 뒷받침되는 선택지",
    "success": "성공하는 법 — 근거로 뒷받침되는 선택지",
    "fashion": "패션 트렌드 — 근거로 뒷받침되는 선택지",
    "relationships": "연애심리 — 근거로 뒷받침되는 선택지",
}
# 구 lifestyle 필러 — reel.py 의 배경음 매핑과 맞춘다
AUDIO_NAME["lifestyle"] = AUDIO_NAME["aging_news"]


def reel_audio_name(spec: dict) -> str:
    handle = spec.get("handle", "@your_ground_zero").lstrip("@")
    label = AUDIO_NAME.get(spec.get("pillar", ""), "근거로 뒷받침되는 선택지")
    return f"{label} · {handle}"


def publish_reel(spec: dict, ig_id: str, token: str, base_url: str, dry: bool = False) -> str | None:
    """카드뉴스 슬라이드로 만든 릴스(mp4)를 발행한다."""
    caption = build_caption(spec)
    url = f"{base_url.rstrip('/')}/out/{spec['slug']}/{spec['slug']}_reel.mp4"

    print(f"▸ [릴스] {spec['slug']} · 캡션 {len(caption)}자")
    check_reachable([url], expect=None)
    print("  영상 접근 확인 완료")

    if dry:
        print("  [dry-run] 여기서 중단합니다.")
        print("   ", url)
        return None

    # 배경음은 reel.py 가 필러에 맞춰 직접 합성한 오리지널 오디오다.
    # audio_name 은 오리지널 오디오에만 붙일 수 있고 한 번 정하면 못 바꾼다.
    # 이름 붙이기는 부가 기능이므로, 거부당하면 이름 없이 그대로 발행한다 —
    # 무인 실행에서 이것 때문에 발행 자체가 실패하면 안 된다.
    fields = dict(media_type="REELS", video_url=url, caption=caption, access_token=token)
    try:
        container = post(f"/{ig_id}/media", audio_name=reel_audio_name(spec), **fields)
    except RuntimeError as e:
        print(f"  audio_name 거부됨 — 이름 없이 발행합니다: {str(e).splitlines()[0]}")
        container = post(f"/{ig_id}/media", **fields)
    print(f"  릴스 컨테이너 {container['id']} — 영상 처리 대기 중")
    wait_ready(container["id"], token, tries=60, delay=10)

    published = post(f"/{ig_id}/media_publish", creation_id=container["id"], access_token=token)
    media_id = published["id"]

    info = get(f"/{media_id}", fields="permalink,timestamp", access_token=token)
    print(f"✅ 릴스 발행 완료 → {info.get('permalink')}")
    return media_id


# ─────────────────────────────────────────────────────────────
def load_queue() -> list[dict]:
    if not os.path.exists(QUEUE):
        return []
    return json.load(open(QUEUE, encoding="utf-8"))


def save_queue(q: list[dict]) -> None:
    json.dump(q, open(QUEUE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def due_candidates(q: list[dict], now: datetime) -> list[tuple[str, dict, str]]:
    """예정 시각이 지난 pending 을 최신 순으로 돌려준다.

    같은 글의 캐러셀/릴스는 각각 독립된 항목으로 취급한다.
    """
    due: list[tuple[str, dict, str]] = []
    for e in q:
        if (e.get("status") == "pending"
                and datetime.fromisoformat(e["publish_at"]) <= now):
            due.append((e.get("format", "carousel"), e, e["publish_at"]))
        if (e.get("reel_status") == "pending"
                and e.get("reel_publish_at")
                and datetime.fromisoformat(e["reel_publish_at"]) <= now):
            due.append(("reel", e, e["reel_publish_at"]))
    due.sort(key=lambda c: c[2], reverse=True)
    return due


def published_today(q: list[dict], now: datetime) -> bool:
    today = now.astimezone(KST).date()
    for e in q:
        for key in ("published_at", "reel_published_at"):
            if e.get(key) and datetime.fromisoformat(e[key]).astimezone(KST).date() == today:
                return True
    return False


def hold_entry(kind: str, entry: dict, reason: str, error: str | None = None) -> None:
    key = "reel_status" if kind == "reel" and entry.get("format") != "reel" else "status"
    entry[key] = "held"
    entry["held_at"] = datetime.now(KST).isoformat()
    entry["hold_reason"] = reason
    if error:
        entry["error"] = error[:1000]


def publish_entry(kind: str, entry: dict, q: list[dict], ig_id: str, token: str,
                  base: str, dry: bool) -> None:
    """1건을 발행하고 결과를 큐에 즉시 기록한다.

    save_queue 를 건건이 부르는 게 핵심이다. 여러 건을 도는 중에 러너가 죽어도,
    이미 인스타에 나간 글은 published 로 남아야 다음 실행이 같은 글을 또 올리지
    않는다(2026-08-22 bib-gourmand 중복 발행 참고).
    """
    spec_path = os.path.join(ROOT, "content", f"{entry['slug']}.json")
    spec = json.load(open(spec_path, encoding="utf-8"))
    validate_rights(spec)

    if kind == "reel":
        media_id = publish_reel(spec, ig_id, token, base, dry=dry)
        if media_id and entry in q:
            if entry.get("format") == "reel":
                entry["status"] = "published"
            else:
                entry["reel_status"] = "published"
            entry["reel_media_id"] = media_id
            entry["reel_published_at"] = datetime.now(KST).isoformat()
            entry.pop("error", None)
            save_queue(q)
        return

    media_id = publish(spec, ig_id, token, base, dry=dry)
    if media_id and entry in q:
        entry["status"] = "published"
        entry["media_id"] = media_id
        entry["published_at"] = datetime.now(KST).isoformat()
        entry.pop("error", None)
        save_queue(q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slug", help="큐를 무시하고 특정 글 발행")
    ap.add_argument("--reel", action="store_true", help="캐러셀 대신 릴스(mp4)로 발행 (--slug 필수)")
    ap.add_argument("--max", type=int, default=DEFAULT_MAX_PER_RUN,
                    help="호환용 옵션. 안전 정책상 자동 실행은 항상 최대 1건입니다.")
    args = ap.parse_args()

    if args.reel and not args.slug:
        sys.exit("--reel 은 --slug 와 함께 사용해야 합니다.")

    ig_id = os.environ.get("IG_USER_ID")
    token = os.environ.get("IG_ACCESS_TOKEN")
    base = os.environ.get("IMAGE_BASE_URL")
    missing = [k for k, v in
               {"IG_USER_ID": ig_id, "IG_ACCESS_TOKEN": token, "IMAGE_BASE_URL": base}.items()
               if not v]
    if missing and not args.dry_run:
        sys.exit(f"환경변수가 없습니다: {', '.join(missing)}")
    if not base:
        sys.exit("IMAGE_BASE_URL이 필요합니다.")

    q = load_queue()
    now = datetime.now(KST)

    if not args.dry_run and published_today(q, now):
        print("오늘(KST) 이미 1건을 발행했습니다. 일일 안전 상한으로 종료합니다.")
        return

    # --slug 는 사람이 특정 글을 콕 집어 올리는 경로다. 큐를 무시하고 1건만.
    if args.slug:
        entry = next((e for e in q if e["slug"] == args.slug),
                     {"slug": args.slug, "status": "pending"})
        kind = "reel" if args.reel else "carousel"
        try:
            publish_entry(kind, entry, q, ig_id, token, base, args.dry_run)
        except Exception as e:
            detail = str(e)
            if entry in q and not args.dry_run:
                reason = ("instagram_action_blocked"
                          if "2207051" in detail or "Application request limit reached" in detail
                          else "publish_failed_manual_review")
                hold_entry(kind, entry, reason, detail)
                save_queue(q)
                print("재시도를 막기 위해 이 항목을 held로 전환했습니다.", file=sys.stderr)
            raise
        return

    # 자동 모드: 가장 최근 due 항목 1건만 선택하고, 밀린 과거 항목은 보류한다.
    candidates = due_candidates(q, now)
    if not candidates:
        print("발행할 차례인 글이 없습니다. 종료.")
        return

    kind, entry, _ = candidates[0]
    if len(candidates) > 1 and not args.dry_run:
        for old_kind, old_entry, _ in candidates[1:]:
            hold_entry(old_kind, old_entry, "backlog_not_auto_published")
        save_queue(q)
        print(f"과거 대기 {len(candidates) - 1}건을 자동 발행하지 않고 보류했습니다.")

    print(f"발행 대상: {entry['slug']} ({kind})")
    try:
        publish_entry(kind, entry, q, ig_id, token, base, args.dry_run)
    except Exception as e:
        detail = str(e)
        msg = detail.splitlines()[0]
        print(f"❌ {entry['slug']} 발행 실패: {msg}", file=sys.stderr)
        if entry in q and not args.dry_run:
            reason = ("instagram_action_blocked"
                      if "2207051" in detail or "Application request limit reached" in detail
                      else "publish_failed_manual_review")
            hold_entry(kind, entry, reason, detail)
            save_queue(q)
            print("재시도를 막기 위해 이 항목을 held로 전환했습니다.", file=sys.stderr)
        sys.exit(f"발행 실패: {entry['slug']}")


if __name__ == "__main__":
    main()
