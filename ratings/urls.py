# ratings/urls.py
from django.urls import path
from . import views




urlpatterns = [
    #path('', views.home, name='home'),
    path('brewery_list/', views.brewery_list, name='brewery_list'),  # Add this line for the root path
    
    path('brewery_detail/<uuid:brewery_id>/', views.brewery_detail, name='brewery_detail'),
    path('add_rating/<uuid:brewery_id>/', views.add_rating, name='add_rating'),
    path('delete_rating/<int:rating_id>/', DeleteRatingView.as_view(), name='delete_rating'),
    path('all_ratings/', views.all_ratings, name='all_ratings'),  # Add this line for all ratings
    path('', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),  # Update this line to use the correct signup view
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutPage, name='logout')
]
