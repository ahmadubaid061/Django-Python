from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello this is home page")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("Hello this is about page")
    return render(request,'about.html')

def services(request):
    return HttpResponse("Hello this is services page")

def contact(request):
    return HttpResponse("Hello this is contact page")