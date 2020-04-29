from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('register/', views.register_page, name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/', views.edit_profile_page, name='edit_profile'),

    path('register_staff/', views.register_staff_page, name='register_staff'),
    path('profile_staff/', views.profile_staff_page, name='profile_staff'),
    path('edit_profile_staff/', views.edit_profile_staff_page, name='edit_profile_staff'),
]
