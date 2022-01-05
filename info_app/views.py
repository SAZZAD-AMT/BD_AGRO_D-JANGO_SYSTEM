from django.shortcuts import render
from info_app.models import InfoModel
from django.db.models import Q


def info_home_view(request):
    posts = InfoModel.objects.all()
    
    search_keyword = request.GET.get('q') or ''
    if search_keyword is not None:
        posts = InfoModel.objects.filter(Q(title__icontains=search_keyword))
    
    context = {
        'posts': posts,
        'search_keyword': search_keyword
    }
    return render(request, 'info/info_home.html', context)


def info_details_view(request, id):
    post = InfoModel.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'info/info_details.html', context)
