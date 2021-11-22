from django.shortcuts import render

from user.decorators import unauthenticated_user


@unauthenticated_user
def home(request):
    return render(request,"home.html")
