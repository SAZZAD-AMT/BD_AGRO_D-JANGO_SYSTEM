from django.shortcuts import render
from user.decorators import unauthenticated_user


@unauthenticated_user
def statistic_view(request):
    return render(request, "statistics/statistic.html")


def k18_view(request):
    return render(request, "statistics/k18.html")
