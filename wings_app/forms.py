from django import forms
from django.forms import ModelForm
from .models import *


class PaperForm(ModelForm):
    image = forms.ImageField(required=True, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = PaperModel
        fields = '__all__'
        exclude = ['author']
