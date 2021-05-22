from django.shortcuts import render
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import *


def index(request):
    all_tags = Tag.objects.annotate(tag_count=Count('posts'))
    query_search = request.GET.get('search', '')
    query_list = request.GET.getlist('tag')

    if query_list and query_search:
        all_posts = Post.objects.filter(tags__tag_name__in=query_list).filter(
            Q(post_text__icontains=query_search) | Q(tags__tag_name__icontains=query_search)).distinct()

    elif query_search:
        all_posts = Post.objects.filter(
            Q(post_text__icontains=query_search) | Q(tags__tag_name__icontains=query_search)).distinct()
    elif query_list:
        all_posts = Post.objects.filter(tags__tag_name__in=query_list).distinct()
    else:
        all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 2)
    pag_number = request.GET.get('page', 1)
    page = paginator.get_page(pag_number)

    is_paginated = page.has_other_pages()

    page_url = '?'

    if query_list:
        for tag in query_list:
            page_url += 'tag={}&'.format(tag)
        page_url += 'page='

    elif query_search:
        page_url = '?search={}&page='.format(query_search)
    else:
        page_url = '?page='

    if page.has_previous():
        if query_list:
            prev_url = '?'
            for tag in query_list:
                prev_url += 'tag={}&'.format(tag)
            prev_url += '&page={}'.format(page.previous_page_number())
        elif query_search:
            prev_url = '?search={}&page={}'.format(query_search, page.previous_page_number())
        else:
            prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        if query_list:
            next_url = '?'
            for tag in query_list:
                next_url += 'tag={}&'.format(tag)
            next_url += '&page={}'.format(page.next_page_number())
        elif query_search:
            next_url = '?search={}&page={}'.format(query_search, page.next_page_number())
        else:
            next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'all_posts': page.object_list,
               'all_tags': all_tags,
               'page_object': page,
               'is_paginated': is_paginated,
               'query_list': query_list,
               'query_search': query_search,
               'next_url': next_url,
               'prev_url': prev_url,
               'page_url': page_url
               }
    return render(request, 'bot_link/index.html', context)
