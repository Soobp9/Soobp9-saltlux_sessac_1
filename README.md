# 챗봇을 활용한 의료가이드 제공 서비스 HealthBot 개발 프로젝트

## Soobp9-saltlux_sessac_
## - readme.md 꼼꼼히 작성하기!!!!!
## - sequence diagram 그리기 <br><br><br><br>

# 본 서비스
## 1. 사용자 주관적 증상 입력 후 대화를 통해 챗봇이 예상 질환, 진료과 추천
## 2. 현재 위치 기반하여 주변 병원 추천 (3. 서비스 비율 순)
## 3. 병원 리뷰 분석(진료과 별 네이버 리뷰 감정 긍정 비율 순) <br><br><br><br>

# 가능한 추가 서비스
## - 동네 병원, 종합병원 진료과 나눠서 추천
## - 약 성분분석(이미지에서 텍스트 추출)
## - 건강기능식품 추천
## - 음성 대화 기능 <br><br><br><br>


# 설치 및 시작
## - 로컬환경에서만 실행 가능
## - vscode에서 live server 확장 프로그램 다운로드
## - 설치
$pip install python-dotenv <br>
$pip install openai <br>
$pip install fastapi <br>
$pip install uvicorn <br>
$pip install jinja2 <br>
$pip install pymongo <br>
## - main_db_1.py 실행
$python -m uvicorn main:app --reload <br>
## - chatbot.html 파일 열어놓은 상태에서 live server 실행 <br><br><br><br>

# 20231123 목요일
## - 증상 데이터 완성 <br><br><br><br>

# 20231124 금요일
## - 음성데이터 신청 및 기획안 작성 - 김수빈
## - 리뷰데이터 크롤링 -금천구 +a(구로구, 관악구) - 강태성, 배해빈
## - 증상 데이터 학습방안 및 구체화 - 이동환
## - 화면구성 및 DB구조 설정 - 손예진, 문재원
## - 시퀀스 다이어그램 그리기, 추가 서비스 고민 - 전체 <br><br><br><br>

# 20231127 월요일
## - 증상 데이터 파일 전처리 - 김수빈, 이동환
## - 중랑구 한정 긍,부정 비율 출력 시도 - 강태성, 배혜빈
## - 크롤링 계속 진행
## - 프로젝트 생성 및 패키지 구성 - 문재원, 손예진 <br><br><br><br>

# 20231128 화요일
## - 초기 모델 구현 - 질의->응답  - 김수빈, 이동환 
## - 리뷰 긍부정 이진분류, 다중분류 - 강태성, 배혜빈
## - 회원가입 / 병원 정보 페이지 기능 구현 - 문재원, 손예진 <br><br><br><br>

# 20231129 수요일
## - 새로운 학습모델 찾기 및 강사님과 상의  - 김수빈, 이동환
## - 깃 브랜치 생성(+ 하위 브랜치, 브랜치 플로우)
## - 리뷰 긍부정 비율 맞추기, 공공데이터와 병합방법 찾기 - 강태성, 배혜빈
## - 로그인 / 병원 정보 페이지 기능 구현 - 문재원, 손예진 <br><br><br><br>


#  2023121 
## 워드클라우드 이미지 생성 - 강태성 <br><br><br><br>

# ~ 20231212 
## 서버 연결하기 fast api, flask 시도 - 전체
## 리뷰데이터 정제 및 긍부정 비율 데이터 만들기 - 강태성 <br><br><br><br>


# 20231214
## 벡터DB 입력 - 1. 기존 데이터 업로드 2. 대화내용 업로드 - 김수빈, 배혜빈, 강태성, 이동환
## 진료과, 리뷰 데이터 연결 - 손예진, 문재원
## 서비스 전체 흐름 시연 - 전체 <br><br><br><br>


# 20231215
## 전체 서비스 연결 - 전체 <br><br><br><br>


# 20231216 토요일
## pt 준비 - 김수빈, 배혜빈
## 파인콘 연결 및 고도화 - 이동환
## 프론트 화면 설정 및 고도화 - 문재원
## 챗봇과 백엔드 연결 - 손예진 <br><br><br><br>

# 20231218 월요일
## 코딩 테스트 - 전체 ㅋㅋㅋ
## 파인콘, 몽고디비 고도화 계속
## 프롬프트 발전

# 20231219
# 20231220

# 20231221
## 발표
