# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("HELLO WORLD! I'M HOME.")

# def about(request):
#     return HttpResponse('MY ABOUT PAGE.')

from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')
    
# def homepage(request):
#     return render(request, '')