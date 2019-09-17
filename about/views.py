from django.views.generic import ListView

from about.models import Job, JobDetail


class JobListView(ListView):
    template_name = 'about/index.html'
    context_object_name = 'job'
    model = Job

    def get_queryset(self):
        _queryset = super().get_queryset()
        return [p for p in _queryset if p.display_on_site]
