from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from blog import models


class BlogListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'all_blogs'
    model = models.BlogPost
    # all_posts = BlogPost.objects.filter(date_published__lte=timezone.now()).order_by('date_published')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['all_posts'] = self.all_posts
    #
    #     return context

    # from StackExchange
    # posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    #
    # return render(request, 'blog/post_list.html', {'posts': posts})


class SingleBlogView(TemplateView):
    template_name = 'blog/single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.BlogPost, self.kwargs['id'])

        return context
