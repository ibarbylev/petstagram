from django.urls import path

from accounts import views

urlpatterns = [
    path('profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup_user, name='signup_user'),
]
