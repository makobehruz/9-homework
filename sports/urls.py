from django.urls import path
from . import views

app_name = 'sports'

urlpatterns = [
    path('list/', views.movie_list, name = 'list'),
    path('form/', views.movies_create, name = 'form'),
    path('detail/<int:pk>/', views.movies_detail, name = 'detail'),
    path('update/<int:pk>/', views.movies_update, name = 'update'),
    path('delete/<int:pk>/', views.movies_delete, name = 'delete'),

]

