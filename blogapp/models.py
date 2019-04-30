from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser  , BaseUserManager
# from django.utils.translation import  ugettext_lazy as _
# from django.dispatch import receiver
# from django.db.models.signals import post_save


class Blog(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name='post_like')
    updated=models.DateTimeField(auto_now=True , auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False , auto_now_add=True)
    def __str__(self):
        return self.title

    def half(self):
        return self.body[:50] + "...."

    @property
    def get_absolute_url(self):
        return "/details-/%s/" %(self.slug)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
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


    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profiles', related_query_name='profile')
    phone = models.IntegerField(default=0)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    city=models.CharField(max_length=50,default="", null=True )

    def __str__(self):
        return self.user.username


# class UserManager(BaseUserManager):
#     use_in_migrations=True
# def save(self, *args, *kwargs):
#     u = super(User, self).save(*args, **kwargs)
#     Profile.objects.get_or_create(user=u.id)
#     return u

#
# @receiver(post_save , sender=User)
# def create_user_profile(sender , instance ,  created , **kwargs):
#     print("under create")
#     if created and not instance.is_staff:
#         # attrs_needed = ['_otherfield',]
#         print(kwargs)
#
#         # if all(hasattr(instance, attr) for attr in attrs_needed):
#         print("hello2")
#         Profile.objects.create(user=instance)  #, phone=instance._otherfield
#         print("hello3")
#         instance.profile.save()
#         print("hello1")


# @receiver(post_save , sender=User, weak=False)
# def my_handler(sender , instance ,  created , **kwargs):
#     print("hello1dfsfs")
#
#     if created and not instance.is_staff:
#         attrs_needed = ['_otherfield', ]
#         if all(hasattr(instance, attr) for attr in attrs_needed):
#             Profile.objects.get_or_create(user=instance, phone=instance._otherfield)
#             instance.profiles.save()
#             print("hello1")