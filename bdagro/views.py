from django.shortcuts import render
from bdagro.models import Project

from user.decorators import unauthenticated_user


@unauthenticated_user
def home(request):
    return render(request,"home.html")


def projects(request):
    projects=Project.objects.all()
    context={'projects': projects }
    return render(request, 'projects/projects.html', context)


    
def project(request,pk):
    projectObj=Project.objects.get(id=pk)
    return render( request, 'projects/single-project.html',{'project': projectObj}) 