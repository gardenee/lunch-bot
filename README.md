# LUNCH-BOT FastAPI 클라이언트

FastAPI를 통해 구현한 간단한 클라이언트 애플리케이션입니다.

## 새 환경에서 실행

```bash
# 1. 저장소 복제 후 디렉토리로 이동
git clone <repository-url>  # 혹은 다른 방식으로 코드 전달
cd <project-directory>

# 2. 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경변수 설정 (.env 파일 생성)
cp .env.example .env
# .env 파일을 열어 실제 값으로 수정

# 5. 애플리케이션 실행
python run.py
```

## 환경변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 환경변수를 설정하세요:

```
# slack key
SLACK_BOT_TOKEN=
SLACK_TEAM_ID=

# 애플리케이션 설정
PORT=8888

# OPENAI 설정
OPENAI_API_KEY=

# OpenWeather API key
OPENWEATHER_API_KEY=

# 카카오 검색 API key
KAKAO_ACCESS_TOKEN=

```

> 참고: `.env` 파일은 민감한 정보를 포함하므로 `.gitignore`에 추가되어 있어 저장소에 포함되지 않습니다.

## API 문서

애플리케이션을 실행한 후, 다음 URL에서 Swagger UI로 API 문서를 확인할 수 있습니다:

- http://localhost:8888/docs
