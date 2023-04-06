from django.db import models
# 데이터베이스의 사용을 더 쉽게 해줄 ORM, 데이터베이스와 Django의 상호 작용기능 import
from django.contrib.auth.models import AbstractUser
# 유저 정보들의 데이터베이스가 담긴 AbstractUser를 import한다.
# 내장된 정보, username,password,email,fist-last name,로그인 및 가입 날짜 활성여부 등등..

class UserModel(AbstractUser):
    #장고의 기본 모델을 상속받는다.
    class Meta:
        db_table = "my_user"
        #데이터 베이스 테이블 이름 지정
