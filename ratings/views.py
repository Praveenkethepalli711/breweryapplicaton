# ratings/views.py
import requests
from django.shortcuts import render, get_object_or_404,HttpResponse,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Brewery, Rating
from .forms import RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def add_rating(request, brewery_phone):
    brewery = get_object_or_404(Brewery, phone=brewery_phone)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.brewery = brewery
            rating.save()
            return HttpResponseRedirect('/ratings/')
    else:
        form = RatingForm()

    context = {'brewery': brewery, 'form': form}
    return render(request, 'ratings/add_rating.html', context)

def delete_rating(request, rating_id):
    # Retrieve the rating object from the database
    rating = get_object_or_404(Rating, id=rating_id)

    if request.method == 'POST':
        # Process the delete request
        rating.delete()
        return HttpResponseRedirect('/ratings/')  # Redirect to the ratings page

    context = {'rating': rating}
    return render(request, 'ratings/delete_rating.html', context)

def brewery_detail(request, brewery_phone):
    brewery = get_object_or_404(Brewery, phone=brewery_phone)
    return render(request, 'ratings/brewery_detail.html', {'brewery': brewery})

def brewery_list(request):
    api_url = 'https://api.openbrewerydb.org/v1/breweries'
    response = requests.get(api_url)
    breweries = response.json()

    context = {'breweries': breweries}
    return render(request, 'ratings/brewery_list.html', context)

def all_ratings(request):
    ratings = Rating.objects.all()
    return render(request, 'ratings/all_ratings.html', {'ratings': ratings})

def ratings(request):
    # Your view logic here
    ratings = Rating.objects.all()
    return render(request, 'ratings/ratings.html')

def profile(request):
    return render(request, 'ratings/profile.html')

@login_required(login_url='ratings/login.html')

#def home(request):
    #return render(request, 'ratings/home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('ratings/login.html')
        



    return render (request,'rtings/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'ratings/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('ratings/login.html')