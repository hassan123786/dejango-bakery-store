from django.shortcuts import render
from django.http import HttpResponse
from mangement.models import *
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import redirect, render



# Create your views here.
# @login_required(login_url='login')
def index(request):
    p = Product.objects.all()
    return render(request, 'mangement/index.html',{'product':p})

def products(request):
    p = Product.objects.all()
    return render(request, 'mangement/products.html',{'product':p})

def checkout(request):
    return render(request, 'mangement/checkout.html')  

def contact(request):
    return render(request, 'mangement/contact.html')

def about(request):
    return render(request, 'mangement/about.html')

def blog(request):
    return render(request, 'mangement/blog.html')

def testimonials(request):
    return render(request, 'mangement/testimonials.html')

def terms(request):
    return render(request, 'mangement/terms.html')

def productdetails(request):

     return render(request, 'mangement/product-details.html')

def blogdetails(request):
    return render(request, 'mangement/blog-details.html')

def logins(request):
    if request.method=="POST":
        # Get the post parameters

        loginusername=request.POST['Username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")
    return render(request, 'mangement/login.html') 

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for errorneous input
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your account has been created successfully ")
        return redirect('login')
    return render(request, 'mangement/signup.html') 
