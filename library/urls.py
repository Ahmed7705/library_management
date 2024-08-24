from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='index'),
    path('author/', views.author_detail, name='author_detail'),
]
