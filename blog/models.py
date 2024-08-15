from django.db import models


class BlogNews(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=120)
    image = models.ImageField(upload_to='products/category/')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_queryset():
        return BlogNews.objects.all().order_by('id')

