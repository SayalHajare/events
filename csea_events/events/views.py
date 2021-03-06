from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm  
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.

def loginPage(request):
    lform = LoginForm(request.POST or None)
    context ={'form':lform}
    print(request.user.is_authenticated)

    if lform.is_valid():
        print(lform.cleaned_data)
        username = lform.cleaned_data.get('email')
        password = lform.cleaned_data.get('password')
        user = authenticate(request, username = username, password = password)
        
        login(request, user)
        if request.user.is_authenticated:
            return render(request, 'home.html', {'display_id':username})
            
    return render(request, 'login.html', context)

User = get_user_model()
def registerPage(request):
    rform = RegisterForm(request.POST or None)
    context = {
        'form':rform
    }
    if rform.is_valid():
        username = rform.cleaned_data.get('email')
        password = rform.cleaned_data.get('password')
        name = rform.cleaned_data.get('name')
        add_user = User.objects.create_user(username, name, password)
        print(add_user)
    return render(request, 'register.html', context)

