# 여행 개인화 앱

서울에서 여수로 가는 2박 3일 여행 계획을 자동으로 생성하는 앱입니다.

## 기능
- KTX, 지하철, 버스 등 대중교통 경로 조회
- 여수 관광지 추천 및 일정 생성
- 맛집 추천 (돌게장 맛집 포함)
- 구글맵스 연동 및 경로 표시

## 설치

```bash
pip install -r requirements.txt
```

## 설정

1. `.env` 파일 생성
2. 구글 맵스 API 키 설정

```bash
cp .env.example .env
# .env 파일에서 GOOGLE_MAPS_API_KEY 설정
```

## 실행

```bash
python main.py
```
