from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Hello world!!")
    return render(request,"templates/hello/index.html") #Practice/djangoPractice/test_proj/hello/templates/hello/index.html
def greet(request, name):
    return HttpResponse(f"Hello, {name}")