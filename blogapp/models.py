from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser  , BaseUserManager
# from django.utils.translation import  ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save






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
    CATEGORY_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','Transgender')
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="keys", related_query_name="key")
    phone = models.IntegerField(unique=True,default=0)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    city=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.user.username

# class User(AbstractUser):
#     username = None
#     phone =models.IntegerField(_('mobile number'),unique=True)
#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = []
#
# class UserManager(BaseUserManager):
#     use_in_migrations=True
# def save(self, *args, *kwargs):
#     u = super(User, self).save(*args, **kwargs)
#     Profile.objects.get_or_create(user=u.id)
#     return u


@receiver(post_save , sender=User)
def my_handler(sender , instance ,  created , **kwargs):
    print("hello1dfsfs")

    if created:
        Profile.objects.get_or_create(user=instance)
    print("hello1")

@receiver(post_save , sender=User)
def save_user_profile(sender , instance , **kwargs):
    instance.profile.save()
    print("hello2")