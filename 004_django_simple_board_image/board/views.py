from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Image
from .forms import BoardForm, ImageForm

def post_list(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            post = board_form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        board_form = BoardForm()
    return render(request, 'board/post_list.html', {'form': board_form})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

def upload_image(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save()
            # 이미지 파일명을 반환
            return JsonResponse({'image_tag': f'[이미지:{image.image.name}]'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


