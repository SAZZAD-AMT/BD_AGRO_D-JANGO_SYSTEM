from django.shortcuts import render, redirect
from bdagro.models import Project
from django.http import HttpResponse
from user.decorators import unauthenticated_user
from bdagro.forms import ProjectForm


@unauthenticated_user
def home(request):
    return render(request, "home.html")


def agricultural(request):
    projects = Project.objects.all()
    context = {"Agricultural": projects}
    return render(request, "bdagro/agricultural.html", context)


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "bdagro/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "bdagro/single-project.html", {"project": projectObj})


def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "bdagro/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "bdagro/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "bdagro/delete_template.html", context)
