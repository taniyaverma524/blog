from django.contrib import admin
from .models import Blog, Comment , Phoneno
from django.contrib.auth.models import User



class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("comment", "email")

# class UserAdmin(admin.ModelAdmin):
#     readonly_fields = ("username","first_name","last_name","email")

class PhonenoAdmin(admin.ModelAdmin):
    readonly_fields = ("phoneno",)

# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)


admin.site.register(Phoneno,PhonenoAdmin)
