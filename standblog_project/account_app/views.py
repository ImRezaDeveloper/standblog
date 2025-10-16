from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import LoginForm, UserEditForm

# Create your views here.

# loginAuth
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account_app/login.html', {'form': form})
    
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

# edit-info-user
def edit_info_user(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        
        if form.is_valid():
            form.save()
    return render(request, 'account_app/edit-info.html', {'form': form})