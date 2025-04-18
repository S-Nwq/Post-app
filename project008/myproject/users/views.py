from django.shortcuts import render
from . import views

# Create your views here.
def sign_up(request):
    return render(request, "users/sign_up.html")