from django.shortcuts import render ,get_object_or_404
from blogapp.forms import CommentForm


from .models import Blog ,Comment

def home(request):
    blogs=Blog.objects.all().order_by('date')
    return render(request,'first.html',{'blg':blogs})

def blog_detail( request,post_slug):
    blog=Blog.objects.get(slug=post_slug)
    blog_comments = Comment.objects.filter(blog__id=blog.id)
    comment_forms= CommentForm()


    return render(request,'second.html',{'blg1':blog,'blog_comments':blog_comments , "comment_forms":comment_forms})




def show_comment(request,post_slug):
    blog=get_object_or_404(Comment,pk=post_slug)
    if request.method == 'POST':
        comment_show = CommentForm(request.POST)
        if comment_show.is_valid():
            try:


                comment_display=comment_show.cleaned_data["comment"]
                email_display = comment_show.cleaned_data["email"]
            except:
                pass
            # return render(request, 'third.html', {'comment': comment_display,'email':email_display})




