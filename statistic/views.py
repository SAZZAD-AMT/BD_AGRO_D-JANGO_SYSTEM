from django.shortcuts import render


from user.decorators import unauthenticated_user


@unauthenticated_user
def statistic_view(request):
    return render(request,"statistic.html")

def k18_view(request):
    return render(request,"k18.html")





