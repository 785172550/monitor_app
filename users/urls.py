from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('addurl/', views.addURL, name='addurl'),
    path('settings/', views.settings, name='settings'),
]
