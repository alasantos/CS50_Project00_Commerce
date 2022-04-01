from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Item

#class ItemForm( forms.Form ):
#    title = forms.CharField( label='Title', required=True)
#    description = forms.CharField( label='Description')
#    imageUrl = forms.URLField( label='Image URL')
#    startingBid = forms.DecimalField( label = 'Starting Bid')

class ItemForm( ModelForm):
    class Meta:
        model = Item
        fields = ['Title', 'Description', 'ItemImage', 'Category','StartingBid']  

def createListing( request ):
    if request.method == 'GET':
        backdata = {
            'ItemForm' : ItemForm(),
            'message': None
        }
        return render(request, 'auctions/createListing.html', backdata)

    form = ItemForm(request.POST)
    if form.is_valid():
        form.save()

    return render( request, 'auctions/index.html' )

def index(request):
    return render(request, "auctions/index.html")




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
