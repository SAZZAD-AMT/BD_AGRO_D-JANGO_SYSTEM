from django.forms import ModelForm, widgets
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "demo_link", "source_link", "tags"]
