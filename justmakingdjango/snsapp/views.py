from django.shortcuts import render, redirect, get_object_or_404
from .forms import uploadform1, commentuploadform1
from .models import Model1forUpload, Model1forComment

# Create your views here.
def home(request):
    #posts = Model1forUpload.objects.all()
    posts = Model1forUpload.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request.method가 POST일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES' :
        form = uploadform1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    # request.method가 GET일 경우
    else :
        form = uploadform1()
    return render(request, 'post_form.html', {'form':form})


def detail(request, post_id):
    post_detail = get_object_or_404(Model1forUpload, pk=post_id)
    comment_form = commentuploadform1()
    return render(request, 'detail.htmnl', {'post_detail':post_detail, 'comment_form':comment_form})

def new_comment(request, post_id):
    written_comment = commentuploadform1(request.POST)
    if written_comment.is_valid():
        final_written_comment = written_comment.save(commit=False)
        final_written_comment = get_object_or_404(Model1forUpload, pk=post_id)
        final_written_comment.save()
    return redirect('detail', post_id)