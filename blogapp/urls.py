from django.urls import path
from .views import blog_home, blog_detail,signup_page,loginpage,login_verification

app_name = 'blogapp'


urlpatterns = [
    path('',loginpage),
    path('login',login_verification),
    path('signup',signup_page),
    path('homepage', blog_home),
    path('<slug:post_slug>',blog_detail , name="second"),

]
