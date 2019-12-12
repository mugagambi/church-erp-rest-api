from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import root
from core.views import news
from core.views import order_of_service
from core.views import sermons

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', root.api_root),
    path('news/', news.index, name='news_list'),
    path('sermons/', sermons.index, name='sermon_list'),
    path('order-of-service/', order_of_service.index, name='order_of_service'),
])
