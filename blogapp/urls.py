from django.urls import path
from .views import home, blog_detail

app_name = 'blogapp'


urlpatterns = [
    path('', home),
    path('<slug:post_slug>',blog_detail , name="second"),


]
