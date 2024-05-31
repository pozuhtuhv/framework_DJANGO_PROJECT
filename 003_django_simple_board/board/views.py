from django.shortcuts import redirect, render

from board.forms import BoardForm
from board.models import Board


def post_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save()  # 폼 데이터를 데이터베이스에 저장
            return redirect('post_detail', title=post.title, pk=post.pk)
    else:
        form = BoardForm()
    return render(request, 'post_create.html', {'form': form})

def post_detail(request, title, pk):
    post = Board.objects.get(title=title, id=pk)
    if not post:
        return render(request, '404.html')
    return render(request, 'post_detail.html', {'post': post})