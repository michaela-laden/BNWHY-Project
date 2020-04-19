from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentCreateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alteryx/', PostListView.as_view(), name='alteryx'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comments-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
    path('post/new/', PostCreateView.as_view(), name='posts-create')
]