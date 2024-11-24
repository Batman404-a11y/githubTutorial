from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
contentsIL=["Arch","Networking","IP"]
def index(request):
    # return render(request,"homeapp/index.html",{
    #     "contentsIL":contentsIL
    # })
    # return HttpResponse("This is a homeapp test") 
    return render(request,"homeApp/index.html",{
        "contentsIL":contentsIL
    })
def haindex(request):
    return render(request,"homeApp/haindex.html")

def fillit(request):
    return render(request, "homeApp/fillit.html")