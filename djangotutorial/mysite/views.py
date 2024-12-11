from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello your at home page")
    return render(request,'index.html')
    
    
  
def about(request):
    #return HttpResponse("hello your at about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("hello your at contact page")
    return render(request,'contact.html')

