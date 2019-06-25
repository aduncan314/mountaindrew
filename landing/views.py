from django.shortcuts import render


def index(request):
    return render(request, 'landing/index.html', context=None)


def cv(request):
    return render(request, 'landing/cv.html', context=None)
