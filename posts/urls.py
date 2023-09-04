from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllView, name='home'),
    # path('', views.PostListView.as_view(), name='home'),
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('like/<int:pk>/', views.LikeView, name='like_view'),
    path('posts/<int:pk>/', views.PostDetailView, name='post-detail'),
    path('edit/<int:pk>/', views.EditView, name='post-edit'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='post-delete'),
]
