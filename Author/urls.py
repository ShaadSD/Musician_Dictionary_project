from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('admin/', admin.site.urls),
     path('register/',views.register, name='register'),
     path('login/',views.user_login, name='user_login'),
     path('logout/',views.user_logout, name='user_logout'),
     path('profile/',views.profile, name='profile'),
]