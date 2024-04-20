from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def myapp(request):
    return render(request, "mainpage.html")

def test(request):
    return render(request, "test.html")

def loginpage(request):
    return render(request, "loginpage.html")