from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import root
from core.views import news

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', root.api_root),
    path('news/', news.index, name='news_list'),
])
