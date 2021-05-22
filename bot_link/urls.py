from django.urls import path
from .views import *

app_name = 'bot_link'

urlpatterns = [
    path('', index, name='index_url')
]
