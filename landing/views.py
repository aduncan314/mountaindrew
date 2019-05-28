from django.shortcuts import render


# Create your views here.
def index(request):
    content_dict = {
        'my_name': 'Drew',
        'simple_intro': "This is my personal site. It's not too nice, but it has character"
    }
    return render(request, 'index.html', context=content_dict)


def cv(request):
    return render(request, 'cv.html', context=None)
