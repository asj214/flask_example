# flask learn example

### packages
- flask
- sqlalchemy

### 초기 설정  
1. 가상화: python -m venv .venv  
2. 가상화 실행: . .venv/bin/activate  
3. pip update: python -m pip install --upgrade pip  
4. package 설치: pip install -r requirements.txt  
5. .env 파일 생성: cp .env.example .env  
6. .env 파일 작성    
7. database migration  
    7-1. 마이그레이션 셋팅: flask db init  
    7-2. 마이그레이션 파일 생성: flask migrate  
    7-3. 마이그레이션: flask db upgrade  

### 웹서버 실행  
`FLASK DEBUG=1 flask run`  

### url  
http://127.0.0.1:5000  