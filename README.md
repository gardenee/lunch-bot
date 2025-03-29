# FastAPI 클라이언트

간단한 FastAPI 클라이언트 애플리케이션입니다.

## 설치 방법

```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows

# 패키지 설치
pip install -r requirements.txt
```

## 환경변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 환경변수를 설정하세요:

```
# MCP 서버 설정
SLACK_BOT_TOKEN=your_slack_bot_token_here
SLACK_TEAM_ID=your_slack_team_id_here

# 애플리케이션 설정
PORT=9000  # 원하는 포트로 변경 가능
```

> 참고: `.env` 파일은 민감한 정보를 포함하므로 `.gitignore`에 추가되어 있어 저장소에 포함되지 않습니다. 대신 `.env.example` 파일을 참고하여 필요한 환경변수를 설정하세요.

## 실행 방법

```bash
# 방법 1
python run.py

# 방법 2
uvicorn app.main:app --reload
```

## API 문서

애플리케이션을 실행한 후, 다음 URL에서 Swagger UI로 API 문서를 확인할 수 있습니다:

- http://localhost:9000/docs

또는 ReDoc 형식의 문서:

- http://localhost:9000/redoc

## 새 환경에서 실행

```bash
# 1. 저장소 복제 후 디렉토리로 이동
git clone <repository-url>  # 혹은 다른 방식으로 코드 전달
cd <project-directory>

# 2. 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는 venv\Scripts\activate  # Windows

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경변수 설정 (.env 파일 생성)
cp .env.example .env
# .env 파일을 열어 실제 값으로 수정

# 5. 애플리케이션 실행
python run.py
```
