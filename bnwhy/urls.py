"""bnwhy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from bnwhy.api import views
from django.contrib.auth import views as auth_views
from users import views as user_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    # Front end Routes
    path('', include('bnwhy.frontend.urls')),

    # Admin Interface
    path('admin/', admin.site.urls),

    #Registration 
    path('register/', user_views.register, name='register'),

    #Profile
    path('profile/', user_views.profile, name='profile'),

    #Login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    #Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # API Routes
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]
