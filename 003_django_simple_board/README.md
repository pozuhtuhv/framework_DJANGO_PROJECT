# 003_django_simple_board
###### Just Post Upload / Read

http://localhost:8000/ -> 메인 글쓰기<br>
http://localhost:8000/\<int> -> 글 조회

1. pip install requirements.txt
2. python manage.py runserver

python manage.py createsuperuser # admin 계정<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py runserver 0.0.0.0:8000