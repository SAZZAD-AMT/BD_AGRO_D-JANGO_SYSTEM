from django.shortcuts import render
from info_app.models import InfoModel


def info_home_view(request):
    posts = InfoModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'info/info_home.html', context)


def info_details_view(request, id):
    post = InfoModel.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'info/info_details.html', context)
