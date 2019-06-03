from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog               
        fields = ['title','body'] #모델에서 타이틀이랑 바디만 쓸거다라는 뜻


