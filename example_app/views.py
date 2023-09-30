from django.http import HttpResponse;


def index(request):
    return HttpResponse("<b>Hello World</b>"r)

def demo(request):
    return HttpResponse("Hello World, demo")

# Create your views here.
