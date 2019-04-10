from django.urls import path
from .views import home, blog_detail,frontpage

app_name = 'blogapp'


urlpatterns = [
    path('/pop', home),
    path('<slug:post_slug>',blog_detail , name="second"),
    path('',frontpage),


]
