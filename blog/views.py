from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import BlogPost


def blag_view(request):
    return render(request, '', context={})


class BlogView(TemplateView):
    template_name = ''