from django import forms
from .models import PostSblawat

class PostForm(forms.ModelForm):
    class Meta:
        model = PostSblawat
        fields = ['title', 'content']
