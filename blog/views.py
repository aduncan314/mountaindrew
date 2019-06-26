from django.views.generic import ListView, DetailView
from blog import models


class BlogListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'all_blogs'
    model = models.BlogPost


class SingleBlogView(DetailView):
    template_name = 'blog/single.html'
    context_object_name = 'blog_post'
    model = models.BlogPost
