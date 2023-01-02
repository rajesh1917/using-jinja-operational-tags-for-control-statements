from django.shortcuts import render

# Create your views here.

def condition1(request):
    d = {'a':30, 'b':20}
    return render(request,'if.html',d)

def condition2(request):
    d = {'a':10, 'b':20}
    return render(request,'if else.html',d)

def condition3(request):
    d = {'a':1001, 'b':2022 , 'c':20}
    return render(request,'if else if.html',d)