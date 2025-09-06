from django.urls import path
from .views import login, dashboard, profile, settings, logout

urlpatterns = [
    path('users/login/', login, name='user-login'),
    path('users/dashboard/', dashboard, name='user-dashboard'),
    path('users/profile/', profile, name='user-profile'),
    path('users/settings/', settings, name='user-settings'),
    path('users/logout/', logout, name='user-logout'),
]
