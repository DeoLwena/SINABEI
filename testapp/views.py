from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'testapp/inde.html')

def project(request):
    return render (request,'testapp/newproj.html')

def login(request):
    return render (request,'testapp/login.html')

def signup(request):
    return render (request,'testapp/signup.html')

def reports(request):
    return render (request,'testapp/reports.html')

def progress(request):
    return render (request,'testapp/progrss.html')