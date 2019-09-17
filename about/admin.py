from django.contrib import admin

from about.models import Job, JobDetail, Organization

admin.site.register(Job)
admin.site.register(JobDetail)
admin.site.register(Organization)
