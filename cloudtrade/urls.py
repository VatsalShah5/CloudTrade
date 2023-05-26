from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('stockpicker/', views.stockpicker, name='stockpicker'),
    path('stocktracker', views.stocktracker, name='stocktracker'),
    path('list_of_stock/', views.ticker, name='ticker_list'),
    path('about_us/', views.about_us, name='about_us'),
]