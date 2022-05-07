from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('about/', views.about, name='webapp-about'),
    path('webteam/', views.webteam, name='webapp-webteam'),
    path('sports/', views.sports, name='sports'),
]