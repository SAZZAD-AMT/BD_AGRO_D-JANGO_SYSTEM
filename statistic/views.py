from django.shortcuts import render


def statistic_view(request):
    return render(request, "statistics/statistic.html")


def k18_view(request):
    return render(request, "statistics/k18.html")


def up21_view(request):
    return render(request, "statistics/up21.html")
