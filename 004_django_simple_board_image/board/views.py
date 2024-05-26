from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Image
from .forms import BoardForm, ImageForm

def post_create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            post = board_form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        board_form = BoardForm()
    return render(request, 'board/post_create.html', {'form': board_form})

def post_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

def upload_image(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        if not images:
            return JsonResponse({'error': 'No images uploaded'}, status=400)

        image_tags = []
        for image in images:
            image_instance = Image(image=image)
            image_instance.save()
            # 이미지 파일명을 반환
            image_tags.append(f'{image_instance.image.name}')

        return JsonResponse({'image_tags': image_tags})
    return JsonResponse({'error': 'Invalid request'}, status=400)
