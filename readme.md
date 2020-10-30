# flask learn example  

pythonanywhere.com 사이트에서 orator 모듈만 문제인지를 확인하기 위해서 만든 repository  
파이썬 orm(django, sqlalchemy) 들은 relationship 설정이나, migrate 할때 after 기능 부재등으로 인하여   
rails 나 laravel 에 비해서 불편한 점들이 있어서 orator를 사용했는데  
orator 모듈의 생명이 끝난듯 하여 별수 없이 sqlalchemy를 사용해야할지도 모르겠다.  
내가 많이 사용해보질 못해서 그런것일 수 도 있지만...  역시 좀 불편하다.  


### 작업해야할 사항  
1. soft delete 기능  
2. api jwt 토큰 인증  
3. banner web/api 개발  
4. swagger 붙이기  


### packages
- flask  
- Flask-WTF  
- Flask-Script  
- Flask-Migrate  
- Flask-SQLAlchemy  
- mysqlclient  
- python-dotenv  
- email-validator  



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