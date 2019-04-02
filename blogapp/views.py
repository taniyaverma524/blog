from django.shortcuts import render


from blogapp.forms import CommentForm
from .models import *
def home(request):
    blogs=Blog.objects.all().order_by('date')
    return render(request,'first.html',{'blg':blogs})
def full( request):
    blogs1=Blog.objects.all().order_by('date')
    form1 = CommentForm()
    return render(request,'second.html',{'blg1':blogs1,'frm':form1})

def comment1(request, pk):
    if request.method== 'Post':
        form1=CommentForm(request.Post)
        if form1.is_valid():
            comment2=form1.cleaned_data['comment']
            User.objects.create_user(comment3=comment2)
            a={'data':comment3}
            blogs2 = Blog.objects.all().order_by('date')
            return render(request,'third.html',a,{'blg1':blogs2})
