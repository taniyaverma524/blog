from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('second',full),
    path('third',comment1)

]
