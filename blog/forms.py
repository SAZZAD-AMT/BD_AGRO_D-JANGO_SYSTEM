from django import forms
from .models import PostModel, CommentModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ("title", "content", "image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("content",)
