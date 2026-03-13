# cc-bot

Pycord 기반 디스코드 음성 자막 봇 프로젝트입니다.

## 빠른 시작

1. 의존성 설치

```bash
uv sync
```

2. 환경 변수 설정

```bash
cp .env.example .env
```

`.env`를 채웁니다.

3. 실행

```bash
uv run python main.py
```

## 디렉토리 구조

```text
src/
	bot/           # 앱 부트스트랩, 인텐트, 서비스 컨테이너
	commands/      # slash command 코그
	listeners/     # discord 이벤트 리스너 코그
	services/      # 유스케이스 조합 레이어
	infra/         # 로깅, 외부 연동 어댑터
	config/        # 환경변수/설정
```