from django.db import models
from django.utils import timezone


class Category(models.Model):
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()


class BlogPost(models.Model):
    is_published = models.BooleanField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    date_published = models.DateTimeField()

    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.ManyToManyField(Category, verbose_name="Category Tag")

    class Meta:
        ordering = ['date_published', 'date_created']

    def publish(self):
        self.is_published = True
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title}: {self.date_published}'
