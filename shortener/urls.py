from django.urls import path
from . import views

urlpatterns = [
    path('shorten/',views.create_short_url, name='create_short_url'),
    path('urls/', views.list_urls, name='list_urls'), 
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]
