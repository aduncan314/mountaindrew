from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='Blog'),
    re_path('^(?P<pk>[\w]+)/$', views.SingleBlogView.as_view())
]
