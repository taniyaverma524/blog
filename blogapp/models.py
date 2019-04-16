from django.db import models
from django.contrib.auth.models import User

# from django.db.models.signals import post_save


class Blog(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

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


class Profile(models.Model):
    MALE=1
    FEMALE=2
    TRANSGENDER=3
    ROLE_CHOICES=(
        (MALE,"male"),
        (FEMALE,"female"),
        (TRANSGENDER,"transgender"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="keys", related_query_name="key")
    phone = models.IntegerField(unique=True,default=0)
    # birthday = models.DateField(blank=True, null=True)
    gender=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default="")
    city=models.CharField(max_length=50,default="")

#
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile=Profile.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile ,sender=User)