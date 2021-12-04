from django import forms
from .models import *


class InfoForm(forms.Form):
    image = forms.ImageField(required=True, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = InfoModel
        fields = '__all__'
