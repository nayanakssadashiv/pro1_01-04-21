from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to base page</h1>")
def index1(request):
    return render(request,"home.html")
    