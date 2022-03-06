from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path(r'register', views.register, name='register'),
    path(r'login', views.login_user, name='login'),
    path(r'logout', views.logout_user, name='logout'),
    path(r'upload', views.upload_view, name='upload'),
    path(r'profile', views.profile_view, name='profile'),
    path(r'profile_update', views.profile_update, name='profile_update'),

]