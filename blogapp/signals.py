from django.dispatch import receiver
# from django.db.models.signals import post_save
# from blogapp.models import Profile
# from django.contrib.auth.models import User
#
#
# # def create_profile(sender,**kwargs):
# #     if kwargs['created']:
# #         user_profile=Profile.objects.create(user=kwargs['instance'])
#
# # post_save.connect(create_profile ,sender=User)
#
# @receiver(post_save , sender=User)
# def create_user_profile(sender , instance ,  created , **kwargs):
#     if created:
#         Profile.Objects.create(user=instance)
#         print("hello1")
#
# @receiver(post_save , sender=User)
# def save_user_profile(sender , instance , **kwargs):
#     instance.profile.save()
#     print("hello2")
