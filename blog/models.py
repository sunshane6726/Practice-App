from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200) # 제목 길이 할당
    pub_date = models.DateTimeField('date published') # 시간과 관련된 함수를 쓰고 
    body = models.TextField() # 엄청 긴글을 쓸수 있는 박스


    def __str__(self): # 메소드를 확인 해준다. __ 특수메소드 사용
        return self.title

    def summary(self):
        return self.body[:100] # body 의 변수에 넣어서 100글자까지 기입만 되게 작성하여라

# python manage.py makemigration 파이썬 >> 쿼리 해석
# python manage.py migration >> 해석한것을 전달 
# 똑바로 하는 것인지 확인
# 제대로 깃허브가 작동하는지 확인한다.


    