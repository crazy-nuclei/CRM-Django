from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def index(request): 

    if request.user.is_authenticated:
        return render(request, 'crm/index.html')
    
    return redirect('login')








    

    
