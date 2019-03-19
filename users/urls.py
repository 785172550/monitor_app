from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('addurl/', views.addURL, name='addurl'),
    path('sub_email/', views.sub_email, name='sub_email'),
    path('send_test/', views.send_test, name='send_test'),
    path('delete_url/', views.delete_url, name='delete_url'),
]
