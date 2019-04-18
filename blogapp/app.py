from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  django.utils.translation import ugettext_lazy as _
from blogapp.models import my_handler\

class BlogappConfig(AppConfig):
    name='blogapp'
    verbose_name=_('blogaap')

def ready(self):
        post_save.connect(my_handler ,sender=User)
