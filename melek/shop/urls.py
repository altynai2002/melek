from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='main'),
    path('about/', views.aboutUs, name='about'),
    path('animal/<int:pk>', views.animal, name='animal'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('category/<str:foo>/', views.category, name='category'),

]
