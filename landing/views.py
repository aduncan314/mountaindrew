from django.shortcuts import render

# Create your views here.
def index(request):
    content_dict = {
        'my_name': 'Drew'
    }
    return render(request, 'index.html', context=content_dict)

def cv(request):
    return render(request, 'cv.html', context=None)