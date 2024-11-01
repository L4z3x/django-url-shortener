from django.urls import path
from . import views

urlpatterns = [
    path('api/shorten/', views.create_short_url, name='create_short_url'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
    path('api/urls/', views.list_urls, name='list_urls'), 
]
