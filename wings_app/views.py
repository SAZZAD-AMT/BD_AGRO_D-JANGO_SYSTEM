from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user.models import User
from wings_app.forms import PaperForm
from wings_app.models import PaperModel


def wings_home_view(request):
    papers = PaperModel.objects.order_by('-posted_on')
    
    is_expart = False
    if request.user.is_authenticated and request.user.is_expart:
        is_expart = True

    paginator = Paginator(papers, 5)
    page = request.GET.get('page', 1)
    try:
        papers = paginator.page(page)
    except PageNotAnInteger:
        papers = paginator.page(1)
    except EmptyPage:
        papers = paginator.page(paginator.num_pages)

    context = {
        'papers': papers,
        'is_expart': is_expart,
    }
    return render(request, 'wings/wings_home.html', context)


@login_required
def paper_post_view(request):
    task = "Post New"
    form = PaperForm()
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.author = request.user
            paper.save()
            return redirect('wings_home')
        else:
            context = {
                'task': task,
                'form': form,
            }
            return render(request, 'wings/paper_post_edit.html', context)
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'wings/paper_post_edit.html', context)


@login_required
def paper_edit_view(request, paper_id):
    task = "Update"
    paper = PaperModel.objects.get(id=paper_id)
    form = PaperForm(instance=paper)
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('paper_details', paper.id)
        else:
            return redirect('edit-article', paper.id)

    context = {
        'task': task,
        'form': form,
        'paper': paper
    }
    return render(request, 'wings/paper_post_edit.html', context)


def paper_details_view(request, paper_id):
    paper = PaperModel.objects.get(id=paper_id)

    my_paper = False
    if request.user == paper.author:
        my_paper = True

    context = {
        'paper': paper,
        'my_paper': my_paper,
    }
    return render(request, 'wings/paper_details.html', context)


@login_required
def paper_delete_view(request, paper_id):
    paper = PaperModel.objects.get(id=paper_id)
    if request.method == 'POST':
        paper.delete()
        return redirect('wings_home')

    context = {
        'paper': paper,
    }
    return render(request, 'wings/paper_delete.html', context)
