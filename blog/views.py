from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone
from blog import models


class BlogListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'all_blogs'
    model = models.BlogPost


class SingleBlogView(DetailView):
    template_name = 'blog/single.html'
    context_object_name = 'blog_post'
    model = models.BlogPost
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = get_object_or_404(models.BlogPost, self.kwargs['id'])
    #
    #     return context
