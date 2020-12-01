from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.user_profile, name='current_user_profile'),
    path('profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup_user, name='signup_user'),
]
