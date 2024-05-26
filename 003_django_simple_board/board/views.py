from django.shortcuts import redirect, render

from .forms import BoardForm
from .models import Board


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
    post = Board.objects.get(pk=id)
    if not post:
        return render(request, 'board/404.html')
    return render(request, 'board/post_detail.html', {'post': post})