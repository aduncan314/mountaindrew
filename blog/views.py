from django.views.generic import ListView, DetailView

from blog import models


class BlogListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'all_blogs'
    model = models.BlogPost
    paginate_by = 5

    def get_queryset(self):
        _queryset = super().get_queryset()
        return [p for p in _queryset if p.is_published]


class SingleBlogView(DetailView):
    template_name = 'blog/single.html'
    context_object_name = 'blog_post'
    model = models.BlogPost
