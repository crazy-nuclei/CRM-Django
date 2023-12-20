from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def index(request): 

    if request.user.is_authenticated:
        return render(request, 'crm/index.html')
    
    return redirect('login')

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

    return render(request, 'crm/login.html')


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
            return render(request, 'crm/register.html', {'form': form})
    else: 
        form = SignUpForm()
        return render(request, 'crm/register.html', {'form': form})
    

        

    # if request.method == 'POST':
	#     form = SignUpForm(request.POST)
	#     if form.is_valid():
	# 		form.save()
	# 		# Authenticate and login
	# 		username = form.cleaned_data['username']
	# 		password = form.cleaned_data['password1']
	# 		user = authenticate(username=username, password=password)
	# 		login(request, user)
	# 		messages.success(request, "You Have Successfully Registered! Welcome!")
	# 		return redirect('home')
    #     else:
    #         form = SignUpForm()
    #         return render(request, 'crm/register.html', {'form': form})
    
