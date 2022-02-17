# BD_AGRO D-JANGO SYSTEM
<img src="https://github.com/SAZZAD-AMT/BD_AGRO_D-JANGO_SYSTEM/blob/main/static-files/Screenshot%202022-02-17%20235050.png?raw=true">

```
TABLE OF CONTENTS
Topic page
 
Introduction & Motivations ………………………………………………… 3
Challenges ………………………………………………………………… 4-5
Requirements ……………………………………………………………….4- 7
Non-functional Requirements ……………………………………………5
Functional Requirements ……………………………………………….. 5-6
Technologies ……………………………………………………………………..6
UML Use Case Diagram------------------------------------------------------------------7
UML Class Diagram-----------------------------------------------------------------------8
```
---
# Introduction
```
BD Agro System is a service and information providing platform that makes life 
easy and saves time for the farmers who wants to acquire information regarding 
their crops especially, in terms of insecticides and which weather is suitable for 
creating a particular crop in a specific pH of land. Moreover, in case of emergency,
clients can take advice from prominent experts and also Search for a specific item 
or list. Furthermore, they can also order fertilizers and insecticides at the cheapest 
price. This document contains the software requirements specification (SRS) for 
said app.
```
---
# Motivations
```
• The main goal of our app is to give people the opportunity to get services by 
seeking information through an app. For example-if one needs to know 
which insecticides will assists them in growing a specific crop, then they’ll 
have to go to the website and ask experts or go through the saved 
information’s by using search option. 
• Our app is targeted to make life easier for people by providing service. For 
example-In this pandemic, people are at remote areas cannot move freely so 
if they need to buy fertilizer they can’t go to market because of safety issues. 
So, in this situation they can order through website and get the required 
substance.
4
• Through this app clients can give review after taking service and recommend 
for future. All of that information available will be constantly available 
through the app’s intuitive UI.
```
---
# Challenges
```
• Implementing certain features such as searching and ordering in a webapplication.
• Since this project is entirely team driven, we lack any client or uppermanagement feedback. Lacking well-defined client-requirements will make 
the development process a little more difficult.
• Adding to the previous point, since we lack any client-defined deadlines, 
proper time management will also be an issue. To remedy this, the team as 
decided to use the Agile Scrum development method.
• Integrating several APIs into the application and ensuring they work 
properly together.
• Getting the team familiar with technologies they haven’t worked with 
before, namely, Django and Python.
• Making sure the UI isn’t too technical or cluttered and follows the latest 
design trends.
5
• Not being able to test the responsiveness of the app in certain 
devices/platforms the team doesn’t have access to, such as Safari browser 
(iOS), smart-televisions, etc. 
• Internet Explorer probably won’t be able to support many of the app’s
features. However, since IE isn’t very popular with the targeted audience, 
this should be considered a minor hindrance at best.
• Ensuring strict client security and protecting the client’s data.
```
---
# Non-functional Requirements
```
For BD AGRO system types of non-functional requirement 
1. Safety / security Requirement.
2. Environmental Requirement.
3. Usability Requirement.
4. Performance Requirement.
5. Development Requirement
```
---
# Functional Requirements
```
In BD AGRO system need a functional requirement 
1. A user can easily access recommended option following the flow chart.
2. BD AGRO is very user-friendly application. User can see all the current 
option in the menu bar.
3. While using BD AGRO user can get First help, quick replies and solutions.
4. User can see he/her profile, Number, Address, Location Including log out,
log in option.
6
5. User can Order Fertilizer and other agricultural tools from BD AGRO 
Application. The package will be delivered to the users in the correct 
location in 2/3 business day.
6. BD AGRO also give you the suitable season and weather details for 
cultivating crops.
7. BD AGRO gives the best advice to the user by our expert doctors online.
Just click the photo of the crop disease then upload the picture and add 
your location, phone number, our expert doctor will advise the user in the 
description box what will be the solution or medicine for the disease.
8. There will be Agricultural news and Update in the Application so the user 
can get the updated news of the current situation. 
```
# User authentication: Since our app deal with sensitive information about the client’s information, a thorough authentication procedure should be followed.
# Research Feed: If any fresher and user want to post something about there thesis, research paper or anything what related about agriculture they can post from this section.

# Technologies: HTML, CSS, Bootstrap, Database, Python, Django.

# UML Use Case Diagram:
<img src="https://github.com/SAZZAD-AMT/BD_AGRO_D-JANGO_SYSTEM/blob/main/static-files/Drawing1.jpg?raw=true">
# UML Class Diagram:

# Activity Diagram:
 
 
# Sequence Diagram:
 
 
# ER diagram:
 

 
# GUI of BD AGRO:
<img src="https://github.com/SAZZAD-AMT/BD_AGRO_D-JANGO_SYSTEM/blob/main/static-files/Screenshot%202022-02-17%20235213.png?raw=true">
# BD AGRO Home Page :
```
 
Login :
 

Sign Up Page :
 
After Login :
 

STATISTIC Page :
 

 


STATISTIC Till 2020 GDP :
 
 

STATISTIC 2021 GDP :
 
 

Profile Of User : 
 
Update Profile :
 

```

AGRO INFO
Proven Business Strategies is Explained with References 

 
 


 
 


 
 
More Fertilizer Info:
Animated Page Using Hover Effects
 

 
 

 
 

                                                                                Marketing
Create Project 

 
 





Edit the Page
 



Delete the page 






View the Created page
 
---
# WINGS OF AGRICULTURE :
```

This is our research page , only an Expert Author can post his/her research on this page.Normal user can only view this page. User can not edit or delete any paper from this page.










User View :

 
 




Expert view : 
 


Edit page :
 



Delete page :
```
---
 
# Farmer's Doctor
```

Here is the feature where a normal user can post his/her crop problem with His/her Name,Location,Phone number as Discription and post His/her problem there.They can edit and Delete the post they have posted. On the posted Blog An Expert can Give his solution by commenting on the Blog post to let the user know the crops problems 

User view :
 
 
 







Edit  and Update Page:
 


Delete Page :
 



Expert Comments :
 
 
```
---
# Agriculture News 
```

Here is the news part of our aplication where users and expert can view news about agriculture from all round the world.No user or Expert can edit any news from this page only admin can post news here and edit and delete post.

 view:
 
 






admin page:
 

edit and delete :
 


```

---

# BD_AGRO SYSTEM CODING

## INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    'bdagro',
    'user',
    'blog',
    'wings_app',
    "info_app",
    "statistic",
    'widget_tweaks',
]
```
----
## URL of CSE347

```
from django.contrib import admin
from django.urls import path, include
from bdagro import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('user.urls')),
    path('blog/',  include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('projects/', include('bdagro.urls')),
    path('statistic/', include('statistic.urls')),
    path('wings/', include('wings_app.urls')),
    path('news/', include('info_app.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
---
# BD AGRO APPS
```
from django.apps import AppConfig


class BdagroConfig(AppConfig):
    name = 'bdagro'
```
---
## BD AGRO URLS
```
from django.urls import path,include
from . import views


urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('projects/project/<str:pk>/', views.project, name="project"),
    path('projects/create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    path('agricultural/', views.agricultural, name="agricultural_input"),
    path('agricultural/morefertilizer/', views.morefertilizer, name="morefertilizer"),
    
]
```
---
## BD AGRO VIEWS
```
from django.shortcuts import render, redirect
from bdagro.models import Project
from django.http import HttpResponse
from user.decorators import unauthenticated_user
from bdagro.forms import ProjectForm


def home(request):
    return render(request, "home.html")


def agricultural(request):
    projects = Project.objects.all()
    context = {"Agricultural": projects}
    return render(request, "bdagro/agricultural.html", context)


def morefertilizer(request):
    return render(request, "bdagro/morefertilizer.html")


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

```
---
# BLOG APPS
## BLOG ADMIN
```
from django.contrib import admin
from .models import *

admin.site.register(PostModel)
admin.site.register(CommentModel)
```
## blog forms
```
from django import forms
from .models import PostModel, CommentModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ("title", "content", "image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("content",)
```
## blog models
```
from django.db import models
from django.shortcuts import reverse
from user.models import User


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("blog_details", kwargs={"blog_id": self.id})

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

```
## blog views
```
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from .forms import *
from django.http import HttpResponse
from .models import PostModel,CommentModel
from django.db.models import Q
from django.contrib.postgres.search import SearchVector


def blog_home_view(request):
    blogs = PostModel.objects.order_by('-posted_on')
    
    search_keyword = request.GET.get('q') or ''
    if search_keyword is not None:
        blogs = PostModel.objects.filter(Q(author__first_name__icontains=search_keyword) | (Q(author__last_name__icontains=search_keyword) | (Q(title__icontains=search_keyword))))

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
        'search_keyword': search_keyword
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

```
---
# info apps
views apps
```
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
```
----
# STATISTIC APPS
## URLS
```
from django.urls import path
from .views import *

urlpatterns = [
    path("", statistic_view, name="statistic"),
    path("k18/", k18_view, name="k18"),
    path("up21/", up21_view, name="up21"),
]
```
---
# Templates have all HTML file and all images in static-file and media file.
---

# USERS DECORETOR APPS
```
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
```
## USER MODEL
```
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone, password, **other_fields):
        if not username:
            raise ValueError('Username is required!')
        elif not phone:
            raise ValueError('Phone number is required!')

        username = self.model.normalize_username(username)
        user = self.model(username=username, phone=phone, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, phone, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, first_name, last_name, phone, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=15, unique=True, primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    is_expart = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.username
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='user.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```
## USER VIEWS
```
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .decorators import unauthenticated_user

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User





@unauthenticated_user
def signup_view(request):
  form = SignUpForm(request.POST)
  if form.is_valid():
    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    authenticate(username=username, password=password)
    return redirect('login')
  return render(request, 'user/signup.html', {'form': form})


@unauthenticated_user
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
  else:
    form = AuthenticationForm()
  return render(request, 'user/login.html',  {'form': form})


def logout_view(request):
  logout(request)
  return redirect('home')

  
def profile_view(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  print(user)
  print(profile)
  context = {
    'user': user,
    'profile': profile,
  }
  return render(request, "user/profile.html", context)


def profile_update_view(request):
  user = request.user
  profile = Profile.objects.get(user=user)
  user_form = UserForm(instance=user)
  profile_form = ProfileForm(instance=profile)
  
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      return redirect('profile')
    else:
      return redirect('profile_update')

  context={
    'user': user,
    'profile': profile,
    'user_form': user_form,
    'profile_form': profile_form,
    }
  return render(request, "user/profile_update.html", context)
 
```

---
# wings_app
```
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user.models import User
from wings_app.forms import PaperForm
from wings_app.models import PaperModel
from django.db.models import Q


def wings_home_view(request):
    papers = PaperModel.objects.order_by('-posted_on')
    
    search_keyword = request.GET.get('q') or ''
    if search_keyword is not None:
        papers = PaperModel.objects.filter(Q(author__first_name__icontains=search_keyword) | (Q(author__last_name__icontains=search_keyword)|Q(title__icontains=search_keyword)))
    
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
        'search_keyword': search_keyword
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
```
---
# REQUIREMENTS TXT
```asgiref==3.4.1
Django==3.2.9
django-widget-tweaks==1.4.9
Pillow==8.4.0
pytz==2021.3
sqlparse==0.4.2
```
