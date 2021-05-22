from django.shortcuts import render
from .models import *
from .filters import *

def index(request):
    all_posts = Post.objects.all()
    all_tags = Tag.objects.all()
    post_filter = PostFilter(request.GET, queryset=all_posts)
    print(post_filter)