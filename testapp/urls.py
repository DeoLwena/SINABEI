from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('newproj.html/', views.project, name='project'),
    path('progrss.html/', views.progress, name='progress'),
    path('reports.html/', views.reports, name='reports'),
    path('signup.html/', views.signup, name='signup'),
    path('login.html/', views.login, name='login'),

]
