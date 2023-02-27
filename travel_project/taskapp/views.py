from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Q

# Create your views here.
def demo(request):
    obj1=Place.objects.all()
    obj2=Q.objects.all()
    return render(request,'index.html',{'result':obj1,'output':obj2})
# def addition(request):
#     X=int(request.GET['num1'])
#     Y=int(request.GET['num2'])
#     rslt=X+Y
#     return render(request,'result.html',{'result':rslt})

