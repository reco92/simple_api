"""Accounts Urls."""
from rest_framework.routers import DefaultRouter

from words import views

app_name = 'words'
api_router = DefaultRouter()

api_router.register(
    r'', views.ConvertionViewSet, 'convertions')


urlpatterns = api_router.urls
