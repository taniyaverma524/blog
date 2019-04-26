from django.urls import path
from .views import blog_home, blog_detail,signup_page,login_page,log_out,like_post

app_name = 'blogapp'


urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('logout', log_out,name='log_out'),
    path('login',login_page, name='login'),
    path('signup',signup_page,name='signup'),
    path('like_post',like_post, name='like_post'),
    path('details-/<slug:post_slug>/',blog_detail , name="second"),


]
