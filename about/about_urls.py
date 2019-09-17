from django.urls import path

from about.views import JobListView

app_name = 'about'

urlpatterns = [
    path('', JobListView.as_view(), name='About Me')
]