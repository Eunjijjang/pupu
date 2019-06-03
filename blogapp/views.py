from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator #빵칼
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects.all().order_by('-id') 
    blog_list = Blog.objects.all().order_by('-id')
    # 이거를 굳이 왜 나눠주냐면 blogs가 있기 때문에 한번 더 묶어준것
    # 블로그 객체 세개를 한 페이지로 자르고 
    paginator = Paginator(blog_list, 3) #어떤 걸, 몇개씩
    # request된 페이지가 뭔지를 알아내고 그걸 변수에 담는다.
    page = request.GET.get('page')
    # request된 페이지를 얻은 뒤 출력해준다.
    posts = paginator.get_page(page) #식빵 조각들
    return render(request, 'home.html', {'blogs' : blogs, 'posts' : posts})
    # 블로그의 모든 글을 대상으로 blog_list에 넣어준다.



def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id) #식빵
   
    
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
# 1. 입력된 내용을 처리하는 기능 -> post
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): # 폼에 다 입력되었는지 검사하는 함수. (검열)
            post = form.save(commit=False) # 아직 저장하지말아라
            post.pub_date=timezone.now() #폼에서 입력하지 않은 시간을 등록해라
            post.save() #시간을 등록하였으면 저장을 해라.
        return redirect('home') #저장을 하였으면 홈을 띄워라. 
# 2. 한 페이지를 띄워주는 기능 -> get
    else:
        form = BlogPost()
        return render(request,'new.html', {'form':form})
