
from django.shortcuts import render, redirect
from blogapp.forms import CommentForm
from .models import Blog, Comment


def home(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request, 'first.html', {'blg': blogs})


def blog_detail(request, post_slug):
    blog = Blog.objects.get(slug=post_slug)
    blog_comments = Comment.objects.filter(blog__id=blog.id)
    if request.method == "POST":
        comment_show = CommentForm(request.POST)
        if comment_show.is_valid():
            Comment.objects.create(blog=blog, comment=comment_show.cleaned_data['comment'],
                                   email=comment_show.cleaned_data['email'])
            return redirect("/" + post_slug)
        else:

            for field in comment_show.errors :
                comment_show=field

            return render(request, "second.html",
                          {'blg1': blog, 'blog_comments': blog_comments, "comment_forms": comment_show, 'errors': comment_show})
    comment_forms = CommentForm()

    return render(request, 'second.html',
                  {'blg1': blog, 'blog_comments': blog_comments, "comment_forms": comment_forms})











