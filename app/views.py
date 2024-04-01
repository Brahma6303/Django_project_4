from django.shortcuts import render

# Create your views here.

def forms(request):
    return render(request,"forms.html")

def tables(request):
    return render(request,"tables.html")

def kanna(request):
    return render(request,"kanna.html")