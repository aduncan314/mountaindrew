from django.shortcuts import render
from landing.forms import resume_choice_form


# Create your views here.
def index(request):
    content_dict = {
        'my_name': 'Drew',
        'simple_intro': "This is my personal site. It's not too nice, but it has character"
    }
    return render(request, 'index.html', context=content_dict)


def cv(request):
    this_form = resume_choice_form()
    return render(request, 'cv.html', context={'form': this_form})
