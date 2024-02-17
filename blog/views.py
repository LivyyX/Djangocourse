from django.shortcuts import render
from .models import Post
from django.utils import timezone
def post_list(request):
    posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html',{'posts':posts})
