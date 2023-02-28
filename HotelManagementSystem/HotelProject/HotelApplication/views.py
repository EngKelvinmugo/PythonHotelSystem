from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def dashboard(request):
    return render(request,'HotelApplication/dashboard.html')
def homepage(request):
    return render(request,"HotelApplication/index.html") 
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account created successfully")
            return redirect("login")
    context = {
        "form": form
    }        
    return render(request, 'HotelApplication/register.html', context)


def login_page(request):
    if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')
       
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request, user)
           return redirect('dashboard')
       else:
           messages.info(request, "Username or password is incorrect !")
    context = {}
    return render(request, 'HotelApplication/login.html', context)

def userLogout(request):
    logout(request)
    return redirect('login')
