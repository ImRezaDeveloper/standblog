from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

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
    context = {"error": []}
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        if password != repassword:
            context['error'].append('password and repassword are not same!')
            return render(request, 'account_app/register.html', context)

        if email == "":
            context['error'].append("the email field shouldn't be empty!")
            return render(request, 'account_app/register.html', context)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'account_app/register.html', {})