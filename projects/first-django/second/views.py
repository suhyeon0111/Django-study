from django.shortcuts import render
from django.http import HttpResponseRedirect

from second.models import Post
from .forms import PostForm


def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/second/list/')
        
    form = PostForm()  # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
    return render(request, 'second/create.html', {'form': form})



def confirm(request):
    form = PostForm(request.POST)  
    if form.is_valid(): 
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/create/')  # 데이터가 유효하지 않으면 되돌아갑니다.


