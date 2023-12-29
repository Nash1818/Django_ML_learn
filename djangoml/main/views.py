from django.shortcuts import render

# Create your views here.
# Business Logic:

# MVT - Model View Template

from django.http import HttpResponse

def welcome(request):
    return render(request, 'index.html')

def user(request):
    username = request.GET['username']
    print(username)
    return render(request, 'user.html', {'name': username})