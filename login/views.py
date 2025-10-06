from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout



# login function :  

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    
    context = {
        "form":form
    }
    return render(request, 'login.html', context)


# register function : 

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    context ={
        "form":form,
    }
    return render(request, 'register.html', context)


# logout functions: 

def logout_view(request):
    logout(request)
    return redirect("home")