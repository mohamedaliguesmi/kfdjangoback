from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    #just for testing the token
    path('user/', views.get_user),
    path('role/', views.RoleList.as_view()),
    path('role/<int:pk>/', views.RoleDetail.as_view()),
]