from django import template

from django.db.models import Count
from blogapp.models import Blog

register=template.Library()


@register.inclusion_tag("most_commented_posts.html")
def get_most_commented_posts(count=1):
    most_commented=Blog.objects.annotate(total_comment=Count('comment')).order_by('-total_comment')[:count]
    print(most_commented)
    return {'most_commented':most_commented}


