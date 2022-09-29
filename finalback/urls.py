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
    path('arbitrator/', views.ArbitratorList.as_view()),
    path('arbitrator/<int:pk>/', views.ArbitratorDetail.as_view()),
    path('coach/', views.CoachList.as_view()),
    path('coach/<int:pk>/', views.CoachDetail.as_view()),
    path('athlete/', views.AthleteList.as_view()),
    path('athlete/<int:pk>/', views.AthleteDetail.as_view()),
    path('club/', views.ClubList.as_view()),
    path('club/<int:pk>/', views.ClubDetail.as_view()),
    path('profile/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('supporter/', views.SupporterList.as_view()),
    path('supporter/<int:pk>/', views.SupporterDetail.as_view()),
    path('export/csv/', views.export_users_csv),
    path('export/xls/', views.export_users_xls),
    #path('alluser/', views.showthis),
    path('allusers/', views.UserList.as_view()),
    path('allusers/<int:pk>/', views.UserDetail.as_view()),
    path('categorie/', views.CategorieList.as_view()),
    path('categorie/<int:pk>/', views.CategorieDetail.as_view()),
    path('Licences/', views.LicencesList.as_view()),
    path('Licences/<int:pk>/', views.LicencesDetail.as_view()),
    path('Grade/', views.GradeList.as_view()),
    path('Grade/<int:pk>/', views.GradeDetail.as_view()),
    path('Seasons/', views.SeasonsList.as_view()),
    path('Seasons/<int:pk>/', views.SeasonsDetail.as_view()),
    path('Weights/', views.WeightsList.as_view()),
    path('Weights/<int:pk>/', views.WeightsDetail.as_view()),

]