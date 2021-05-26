from django.shortcuts import render
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from urllib.parse import urlencode
from .models import *


def index(request):
    all_tags = Tag.objects.annotate(tag_count=Count('posts'))
    query_search = request.GET.get('search', '')
    query_list = request.GET.getlist('tag')

    all_posts = Post.objects.distinct()

    if query_search:
        all_posts = all_posts.filter(
            Q(post_text__icontains=query_search) | Q(tags__tag_name__icontains=query_search))

    if query_list:
        all_posts = all_posts.filter(tags__tag_name__in=query_list)

    paginator = Paginator(all_posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    url = urlencode([('tag', i) for i in query_list] + [('search', q) for q in query_search])

    if request.is_ajax():
        return JsonResponse({'all_posts': list(all_posts.values())})

    context = {'all_posts': page.object_list,
               'all_tags': all_tags,
               'page_obj': page,
               'query_list': query_list,
               'query_search': query_search,
               'url': url
               }
    return render(request, 'bot_link/index.html', context)
