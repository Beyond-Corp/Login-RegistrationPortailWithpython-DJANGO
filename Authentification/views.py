from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('welome in the home page')




def signup(request):
    return render(request,'auth/signup.html')

def signin(request):
    return render(request,'auth/signin.html')

def signout(request):
    return render(request,'auth/signout.html')
def dashboard(request):
    return render(request,'auth/dashboard.html')