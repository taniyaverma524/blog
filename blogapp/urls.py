from django.urls import path
from .views import home, blog_detail , show_comment

app_name = 'blogapp'


urlpatterns = [
    path('', home),
    path('second/<slug:post_slug>/',blog_detail , name="second"),
    path('third',show_comment),

]
