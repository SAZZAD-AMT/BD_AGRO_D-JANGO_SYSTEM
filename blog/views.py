from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# blog view
@login_required
def blog_view(request):
  return render(request, 'blog.html')