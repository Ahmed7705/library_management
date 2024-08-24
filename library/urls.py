from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='boooks'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),


]
