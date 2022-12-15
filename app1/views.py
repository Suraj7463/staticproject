from django.shortcuts import render

# Create your views here.
def display_image(request):
    res=render(request,"index.html")
    return res
