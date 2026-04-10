from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hey welcome</h1>")
    
    # return render(request,"index.html")
    #sending dynamic data 
    context={
        'name':'Ubaid',
        'age' : 23,
        'degree':'BSCS'
    }
    
    return render(request,'index.html',context)
