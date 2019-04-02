from django.db import models

from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    date = models.DateField(auto_created=True)
    def __str__(self):
        return self.title

    def half(self):
        return self.body[:50] + "...."
    def slug(self):

        return slugify(self.title)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogs', related_query_name='blog')
    comment = models.CharField(max_length=512)
    created = models.DateTimeField(auto_created=True)
    email = models.EmailField()

    def __str__(self):
        return self.blog.title
