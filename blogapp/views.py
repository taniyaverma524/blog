from django.contrib.auth.models import User
from django.shortcuts import render, redirect , HttpResponse
from blogapp.forms import CommentForm, UserForm, ProfileForm
from .models import Blog, Comment, Profile
from django.contrib.auth import authenticate ,login

def loginpage(request):
    return render( request,"login.html")

def signup_page(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if (user_form.is_valid() and profile_form.is_valid() ):




            username=user_form.cleaned_data['username']
            email=user_form.cleaned_data['email']
            first_name=user_form.cleaned_data['first_name']
            last_name=user_form.cleaned_data['last_name']
            password=user_form.cleaned_data['password']


            user= User.objects.create(username=username, last_name=last_name, first_name=first_name, email=email)
            user.set_password(password)

            user.save()
            # # print(user)
            # # User.objects.create(**user_form.cleaned_data)
            #
            # phone = profile_form.cleaned_data.get('phone')
            # birthday= profile_form.cleaned_data.get('birthday')
            # gender = profile_form.cleaned_data.get('gender')
            # city = profile_form.cleaned_data.get('city')
            # Profile.objects.create(user=user, phone=phone,city=city, gender=gender, birthday=birthday)
            return redirect("/homepage")
        else:

            return render(request,"signup.html",{"user_form":user_form,"phone_form":profile_form})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request,"signup.html",{"user_form":user_form,"phone_form":profile_form})


def blog_home(request):
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


def login_verification(request):

    username=request.POST.get('username')
    password=request.POST.get('password')
    if (username.isdigit()):
        user=Profile.objects.get(phone=username).user


        if user.check_password(password):
            return redirect("/homepage")
        else:
            return HttpResponse("<h1> INVALID </h1>")
    else:


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("/homepage")
        else:
            return HttpResponse("<h1> INVALID </h1>")






