from django import template
from urllib.parse import urlencode

register = template.Library()


@register.filter(name='urlenc')
def urlenc(query_list, query_search):
    return urlencode([('tag', i) for i in query_list] + [('search', query_search)])
