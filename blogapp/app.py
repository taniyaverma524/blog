from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  django.utils.translation import ugettext_lazy as _
from blogapp.models import my_handler ,save_user_profile
class BlogappConfig(AppConfig):
    name='blogapp'
    verbose_name=_('blogaap')

def ready(self):
        post_save.connect(my_handler ,sender=User)
        post_save.connect(save_user_profile ,sender=User)
        print("hello2")