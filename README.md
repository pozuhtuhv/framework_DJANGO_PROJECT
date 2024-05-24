# Django_Project

###### 001_django_basic_api : 기초 API 서비스 구축
###### 002_django_basic_board : 기초 보드 폼 구축
###### 003_django_simple_board : Just Post Upload / Read

http://localhost:8000/ -> 메인 글쓰기<br>
http://localhost:8000/\<int> -> 글 조회

1. pip install requirements.txt
2. python manage.py migrate
3. MySQL -> django_test -> 'Create Table' -> 'board_board' -> 'Create Table' -> 'board_image'
4. config -> settings.py -> ALLOWED_HOSTS -> 내부아이피 설정
5. python manage.py runserver

python manage.py migrate --fake {appname} zero<br>
python manage.py migrate {appname}<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py createsuperuser # admin 계정<br>
python manage.py runserver