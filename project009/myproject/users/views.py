from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    form = UserCreationForm()
    return render(request, "users/sign_up.html" , { "form":form })