from django import forms
from .models import Board, Image

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'username', 'content']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']