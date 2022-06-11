from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm


# 기본 페이지를 띄우는 함수(처음 시작페이지)
def home(request) :
    # 블로그 글들을 띄우는 코드가 필요함.
    #posts = Blog.objects.all() #블로그 객체들을 모조리 갖고와서 posts 변수에 담는다. 이건 그냥 다 쓸어오는거고
    posts = Blog.objects.filter().order_by('date') #이렇게 하면 날짜순으로 쓸어오는 것
    return render(request, 'index.html', {'posts':posts})

# 글을 작성하는 페이지를 띄우는 함수(새 글쓰기를 눌렀을 때)
def new(request) :
    return render(request, 'new.html')

# 작성한 글을 업로드하는 기능을 가진 함수(submit 버튼을 눌렀을 때)
def create(request) :
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# Django form을 이용해서 입력값을 받는 함수로
# GET요청(입력값을 받을 수 있는 html을 가져오라는 요청)
# POST요청(입력한 내용을 데이터베이스에 저장하라는 요청. Form에서 입력한 내용을 처리하라는 요청)
# 둘 다를 처리할 수 있는 함수
def formcreate(request):
    if request.method == 'POST' :
        #입력 내용을 데이터베이스에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            #저장을 시행하라는 코드
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 HTML을 가져다주기
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})


def modelformcreate(request):
    if request.method == 'POST' or request.method == "FILES":
        #입력 내용을 데이터베이스에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            #저장을 시행하라는 코드
            form.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 HTML을 가져다주기
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # Blog_id 번째 블로그 글을 데이터베이스로부터 끌고 온 다음에
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail' : blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)

 