from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('profile/', views.profile_page, name='profile'),
]
