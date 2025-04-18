from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    form = UserCreationForm()
    return render(request, "users/sign_up.html" , { "form":form })

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect ("posts:list")
            
    else:
        form = AuthenticationForm()
    return render(request, "users/sign_in.html", { "form": form })