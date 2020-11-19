from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pets, name='list pets'),
    path('create/', views.pet_create, name='pet_create'),
    path('delete/<int:pk>/', views.pet_delete, name='pet_delete'),
    path('details/<int:pk>/', views.show_pets_details_and_commits, name='pet details'),
    path('edit/<int:pk>/', views.pets_edit, name='pets_edit'),
    path('like/<int:pk>/', views.pets_like, name='like pet'),
]
