from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def login_page(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
        else: 
            messages.error(request, 'Invalid username or password.')

        return redirect('index')

    return render(request, 'auth_users/login.html')


def logout_func(request): 
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    else:
        messages.error(request, 'There was an error logging out.')
    
    return redirect('login') 


def register_page(request): 
    
    if request.method == 'POST': 
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            # Authenticate and Login the user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('index')
        else:
            return render(request, 'auth_users/register.html', {'form': form})
    else: 
        form = SignUpForm()
        return render(request, 'auth_users/register.html', {'form': form})