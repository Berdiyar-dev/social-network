from django.urls import path
from . import views
from .views import Register



urlpatterns = [
    path('', Register.as_view(), name='signup'),
    path('profile_edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('register/', views.RegistrationView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('users/', views.AllUsersView, name='users'),
    path('users/<int:pk>/', views.AboutUserView, name='about_user'),
    path('users/<int:pk>/follow', views.AboutUserView, name="follow"),
]

# urlpatterns = [
#     path('', views.RegistrationView, name='register'),
#     path('profile_edit/<int:pk>/', views.profile_edit, name='profile_edit'),
#
#     path('login/', views.LoginView, name='login'),
#     path('users/', views.AllUsersView, name='users'),
#     path('users/<int:pk>/', views.AboutUserView, name='about_user'),
# ]
