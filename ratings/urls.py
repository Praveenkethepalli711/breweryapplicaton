# ratings/urls.py
from django.urls import path
from . import views



urlpatterns = [
    #path('', views.home, name='home'),
    path('brewery_list/', views.brewery_list, name='brewery_list'),  # Add this line for the root path
    path('<str:brewery_phone>/brewery_detail/', views.brewery_detail, name='brewery_detail'),
    path('<str:brewery_phone>/add_rating/', views.add_rating, name='add_rating'),
    path('<str:brewery_phone>/delete_rating/', views.delete_rating, name='delete_rating'),
    path('all_ratings/', views.all_ratings, name='all_ratings'),  # Add this line for all ratings
    path('ratings/', views.ratings, name='ratings'),
    path('', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),  # Update this line to use the correct signup view
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutPage, name='logout')
]
