from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
])
