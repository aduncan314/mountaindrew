from django.contrib import admin
from django.utils import timezone

from blog.models import BlogPost, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'date_created', 'date_published']
    ordering = ['date_created']
    actions = ['publish']

    def publish(self, request, queryset):
        blogs_published = queryset.update(is_published=True, last_updated=timezone.now(), date_published=timezone.now())
        msg = "1 blog published" if blogs_published == 1 else f"{blogs_published} blogs published"
        self.message_user(request, msg)

    publish.short_description = 'Publish blog post(s)'


admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
