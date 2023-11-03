from django.http import HttpResponse;
from django.shortcuts import render;

# Create your views here.

def index(request):
    return HttpResponse("<b>Hello World</b>")

def demo(request):
    return HttpResponse("Hello World, demo")

def templateExample(request):
    context = {
        "title":"My Template Title",
        "data": [
            {
                'name':"BMW 3 series",
                'cost':65000
            },
            {
                'name':"Honda Accord",
                'cost':40000
            },
            {
                'name':"BMW X7",
                'cost':140000
            },
            {
                'name':"Dodge Challenger",
                'cost':86000
            },
            {
                'name':"Hyundai Sonata",
                'cost':35000
            },
            {
                'name':"Ford GT",
                'cost':220000
            }
        ]
    }
    return render(request, 'mytemplate.html',context)

def temp(request):
    return HttpResponse("DEMO")

def imageDemo(request):
    context = {
        "imgUrl" : "https://m.media-amazon.com/images/I/81ZCOEc-b0L._SL1500_.jpg"
    }
    return render(request, 'imagetemplate.html', context)
