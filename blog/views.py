from django.shortcuts import redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from .forms import *


def blog_home_view(request):
    blogs = PostModel.objects.order_by('-posted_on')

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_home.html', context)


def blog_post_view(request):
    task = "Post a New"
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_details', blog.id)
        else:
            context = {
                'task': task,
                'form': form,
            }
            return render(request, 'blog/blog_post_edit.html', context)
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'blog/blog_post_edit.html', context)


def blog_edit_view(request, blog_id):
    task = "Update"
    blog = PostModel.objects.get(id=blog_id)
    form = PostForm(instance=blog)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_details', blog.id)
        else:
            return redirect('blog_edit', blog.id)

    context = {
        'task': task,
        'form': form,
        'blog': blog
    }
    return render(request, 'blog/blog_post_edit.html', context)


def blog_details_view(request, blog_id):
    blog = PostModel.objects.get(id=blog_id)
    comments = CommentModel.objects.filter(post=blog)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = blog
            comment.save()
            return redirect('blog_details', blog.id)
        else:
            return redirect('blog_details', blog.id)

    my_blog = False
    if request.user == blog.author:
        my_blog = True

    context = {
        'my_blog': my_blog,
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/blog_details.html', context)


def blog_delete_view(request, blog_id):
    blog = PostModel.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_home')

    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_delete.html', context)
