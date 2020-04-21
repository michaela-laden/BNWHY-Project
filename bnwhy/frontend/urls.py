from django.urls import path
from .views import AlteryxListView, SQLListView, ShareListView, PythonListView, OCRListView, BlueListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentCreateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alteryx/', AlteryxListView.as_view(), name='alteryx'),
    path('sql/', SQLListView.as_view(), name='sql'),
    path('sharepoint/', ShareListView.as_view(), name='sharepoint'),
    path('R-python-vba/', PythonListView.as_view(), name='R-python-vba'),
    path('ocr/', OCRListView.as_view(), name='ocr'),
    path('blue-prism/', BlueListView.as_view(), name='blue-prism'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comments-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
    path('post/new/', PostCreateView.as_view(), name='posts-create')
]