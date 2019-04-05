from django.db import models




class Blog(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.blog.title

    def half(self):
        return self.body[:50] + "...."


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogs', related_query_name='blog')
    comment = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return self.blog.title

    class Meta:
        ordering = ('-created',)