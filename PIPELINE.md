# 일일 자동 파이프라인 (클라우드 실행 기준)

이 문서는 **`.github/workflows/daily-content.yml` 이 실행하는 에이전트가
그대로 따라 하는 절차서**입니다. ig-studio(@your_ground_zero)의 동일 파이프라인을
음식/카페/바 안내 계정(@deep_dive_korea)용으로 옮긴 것입니다.
에이전트는 아무 맥락 없이 시작하므로, 이 문서만 읽고도 끝까지 갈 수 있어야 합니다.

전체 그림:

```
daily-content.yml  09:00 / 15:00 KST  →  리서치·집필·렌더링·커밋 (이 문서)
publish.yml        30분마다            →  큐에서 차례 된 글 1건 발행
refresh-token.yml                      →  인스타그램 토큰 갱신
```

전제:
- 작업 디렉터리 = 이 리포지토리의 체크아웃 (경로를 가정하지 말 것. `git rev-parse --show-toplevel` 로 확인)
- 워크플로가 `TZ=Asia/Seoul` 을 걸어두므로 러너의 `date` 는 KST 로 나온다. 다만
  환경이 바뀔 수 있으니 **날짜·요일은 항상 `TZ=Asia/Seoul date` 로 명시해서 구할 것**
  (러너 기본값은 UTC이고, 그대로 쓰면 자정~오전 9시 사이에 날짜가 하루 어긋난다)
- 인스타그램 실제 발행은 **이 에이전트가 하지 않는다.** GitHub Actions 의
  `publish.yml` 이 30분마다 큐를 훑어서 발행한다 (§6 참고)

---

## 0. 시간 예산 — 20분

시작할 때 `date +%s` 값을 기억한다. 리서치 단계마다 경과 시간을 확인한다.

- 15분이 지났는데 검증된 소재가 없으면: 확보된 것으로 마무리하거나, 스킵 노트를 쓰고 중단
- 20분을 넘기면 즉시 중단하고 스킵 노트를 쓴다
- 단, **콘텐츠를 이미 커밋했다면 푸시까지는 반드시 끝낸다.** 예산은 리서치에 걸린 것이지
  정리 작업에 걸린 게 아니다

스킵할 때는 `SKIPPED.md` 를 리포지토리 루트에 쓰고 커밋·푸시한다
(로컬 `/tmp` 는 클라우드 세션이 끝나면 사라져서 아무도 못 본다).
무엇이 없었는지, 다음 실행이 이어받을 수 있게 이미 검증한 자료를 함께 적는다.

## 1. 오늘의 서브카테고리 정하기

```
TZ=Asia/Seoul date +%u    # 1=월 ... 7=일
```

| 요일 | 오전(AM) | 오후(PM) |
|---|---|---|
| 월 | restaurant | cafe |
| 화 | bar | local |
| 수 | restaurant | cafe |
| 목 | bar | local |
| 금 | restaurant | cafe |
| 토 | bar | local |
| 일 | restaurant | cafe |

이 표는 `CONTENT.md` §1 과 일치해야 한다. 어긋나면 **CONTENT.md 를 신뢰**하고
그쪽 기준으로 진행한다.

## 2. 쓰기 전에 기준부터 읽는다

- `CONTENT.md` 전문 — 특히 §2 톤 규칙, §3 슬라이드 구조와 표지 스키마, §4 캡션 구조(~250자), §5 해시태그
- `scripts/cardnews.py` — 슬라이드 타입별 정확한 JSON 필드명
- 오늘 서브카테고리의 최근 콘텐츠 2~3건 (`ls content/`, 같은 필러 파일을
  `grep '"pillar": "<서브카테고리>"' content/*.json` 로 찾는다)
  — **같은 날 다른 슬롯이 이미 올린 것 포함**해서 같은 가게·같은 동네를 반복하지 않는다

### ⚠️ 슬롯 중복 확인 — 쓰기 전에 반드시

주제 겹침과는 **별개의 확인**이다. 오늘 이 슬롯이 이미 채워졌는지를 본다.
재시도·수동 실행·크론 중복 실행 때 같은 슬롯에 두 번째 글이 올라가는 걸 막는다.

```
TZ=Asia/Seoul date +%F        # 오늘 날짜
grep -l "\"pillar\": \"<오늘 서브카테고리>\"" content/<오늘날짜>-*.json 2>/dev/null
```

오늘 날짜 + 오늘 서브카테고리 조합이 이미 `content/` 에 있고 그 슬러그가 `queue.json` 에서
`published` 이거나 `pending` 이면, **이 슬롯은 이미 처리된 것이다.**
새 글을 만들지 말고 "슬롯 이미 채워짐 — 건너뜀"이라고 보고하고 즉시 종료한다.

(월/수/금/일 오전은 restaurant, 오후는 cafe 로 반복되지만 날짜가 다르므로 슬롯 충돌은 없다.
날짜+서브카테고리 조합으로 슬롯이 특정된다.)

## 3. 검증 규칙 — 타협 없음, 특히 실존 확인

이 계정 전체가 "실재하고 지금 영업 중인 곳"이라는 신뢰 위에 서 있다.
모든 게시물에 대해 **가게 이름·주소·현재 영업 여부를 실제 검색으로 확인**한다
(네이버지도·카카오맵·캐치테이블·다이닝코드 같은 예약/리뷰 플랫폼, 공식 인스타그램/웹사이트,
최근 1~2년 내 신뢰할 만한 언론 보도 중 최소 하나). 확신이 없으면 **절대 지어내지 말고**
§0 의 스킵 절차를 따른다 — 없는 가게를 추천하는 것이 이 계정의 유일한 치명적 실패다.

메뉴·가격·영업시간 등 세부 정보도 실제 출처에 있는 것만 쓴다. "가봤더니 좋더라" 식으로
직접 방문한 것처럼 쓰지 않는다 (리서치 기반 계정임을 톤으로 인정한다 — CONTENT.md §2).

진지하게 찾아봤는데도 오늘 서브카테고리에 맞는 검증 가능한 곳이 없으면
**날조하지 말고** §0 의 스킵 절차를 따른다.

## 4. 작성과 렌더링

`content/<YYYY-MM-DD>-<short-slug>.json` 을 쓴다:

- `pillar` = 오늘의 서브카테고리 키 (restaurant/cafe/bar/local), `handle` = `"@deep_dive_korea"`
- `publish_at` = 지금 시각 (`TZ=Asia/Seoul date +%Y-%m-%dT%H:%M:%S+09:00`)
- 슬라이드 7장: cover / stat / list / point / list / quote / source
  (필드명은 `scripts/cardnews.py` 기준. 표지는 eyebrow + 2행 headline("1행 긴장 / 2행 해소")
  + subline + anchor(짧은 숫자·단어). **`bg_image` 는 쓰지 않는다** — 특정 가게의 실제 내부 사진은
  사용 권리를 확인할 수 없는 한 절대 넣지 않는다)
- 캡션 ~250자 (CONTENT.md §4 의 4단 구조)
- 해시태그 ~20개, CONTENT.md §5 의 3계층

그다음 직접 렌더링해서 7장이 오류 없이 나오는지 확인한다:

```
pip install --quiet pillow      # 없을 때만
python3 scripts/cardnews.py content/<slug>.json out
```

**렌더링 결과 이미지(`out/<slug>/`)는 반드시 직접 커밋해야 한다.**
`render.yml` 은 `content/**.json` 푸시에 반응하지만, GitHub Actions 안에서
`GITHUB_TOKEN` 으로 푸시하면 워크플로 재귀 방지 때문에 트리거되지 않는다.
즉 `daily-content.yml` 실행 중에는 render.yml 이 백스톱이 되어주지 않는다.
이미지가 없으면 발행 단계에서 인스타그램에 넘길 URL이 없다.

(사람이 로컬에서 직접 푸시할 때는 render.yml 이 정상적으로 돈다.)

## 5. 큐 등록과 푸시

`queue.json` 배열 끝에 추가한다 (JSON 유효성 유지):

```json
{"slug": "<slug>", "pillar": "<서브카테고리>", "publish_at": "<지금, +09:00 ISO>", "status": "pending"}
```

```
git add content/<slug>.json out/<slug>/ queue.json
git commit -m "content: <slug> (일일 자동 파이프라인, 오전|오후)"
git pull --rebase && git push
```

푸시가 안 되면 거기서 멈추고 **왜 실패했는지 보고**한다. 커밋이 원격에 올라가지 않으면
발행 워크플로가 그 글을 볼 수 없다.

## 6. 발행은 크론이 한다 — 에이전트가 직접 쏘지 않는다

`publish.yml` 이 **30분마다** 돌면서 `queue.json` 의 `status: "pending"` 중
`publish_at` 이 지난 가장 오래된 1건을 발행하고, 큐를 `published` 로 갱신해 커밋한다.

즉 §5 의 푸시가 끝나면 할 일은 끝이다. 최대 30분 안에 자동 발행된다.
단 §4 대로 **이미지까지 함께 커밋했을 때만** 그렇다.

여유가 있으면 결과를 확인해두면 좋다 (`gh` 인증이 없으면 그냥 건너뛴다):

```
gh run list -R steverse-code/deep-dive-korea --workflow=publish.yml --limit 3 \
  --json status,conclusion,createdAt,url
```

**직접 `gh workflow run publish.yml` 을 쏘지 않는다.** 크론과 겹쳐 중복 발행이 날 수 있다.
크론이 30분 넘게 안 돌았다고 확신할 때만 예외로 쓴다.

## 7. 실패했을 때

Meta 쪽 제한 — `Application request limit reached` (code 4, subcode 2207051) 또는
`API access blocked` (OAuthException code 200) — 은 신규 계정에서 게시 속도가 높을 때
Meta 가 거는 레이트리밋이다 (ig-studio 계정이 겪은 적 있다).
**재시도하지 않는다.** 콘텐츠는 이미 커밋·큐에 있으므로 제한이 풀리면 다음 크론이 발행한다.
다른 오류도 마찬가지로 루프 돌며 재시도하지 말고 그대로 보고한다.

## 8. 보고

200자 이내로: 선택한 서브카테고리와 가게, 실존 확인에 쓴 출처, 렌더링 결과,
커밋·푸시 여부, 발행은 크론에 맡겼다는 점.
