from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

# loginAuth
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('user not found!')
    return render(request, 'account_app/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('/')

# Register Auth
def register_user(request):
    return render(request, 'account_app/register.html', {})