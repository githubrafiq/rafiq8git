
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'accounts/profile.html')


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username2 = form.cleaned_data['username']
            print('hello', username, username2)
            messages.success(request, f'Hi {username}! You have created successfully your accounts.')
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/logout.html')


from django.shortcuts import render


