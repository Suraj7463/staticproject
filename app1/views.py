from django.shortcuts import render

# Create your views here.
def display_image(request):
    res=render(request,"test.html")
    return res
