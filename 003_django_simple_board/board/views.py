from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm

def post_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save()  # 폼 데이터를 데이터베이스에 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = BoardForm()
    return render(request, 'board/post_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})
