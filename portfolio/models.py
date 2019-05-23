from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    # 이미지를 쓰기 위해선 필로설치해줘야함 pip install pillow 
    # 필로는 파이썬으로 이미지를 효율적으로 해주게 하는 시스템 
    # pil 파이썬 이미지 라이브러리였다.
    description = models.CharField(max_length=500)
    

    def __str__(self):
        return self.title
