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



   
