from django.db import models


class Category(models.Model):
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    is_published = models.BooleanField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    date_published = models.DateTimeField(null=True, blank=True)

    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.ManyToManyField(Category, verbose_name="Category Tag", blank=True)

    class Meta:
        ordering = ['-date_published', '-date_created']

    def get_preview(self):
        if len(self.content) >= 200:
            return f'{self.content[:197]}...'
        else:
            return self.content

    def get_categories(self):
        return [tag['name'] for tag in self.category.values()]

    def is_edited(self):
        time_diff = self.last_updated - self.date_published
        # Seconds are not cumulative
        return (time_diff.seconds > 30) and (time_diff.days >= 0)

    def __str__(self):
        return self.title
