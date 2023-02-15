from django.shortcuts import render


# Create your views here.
def demo(request):
    name = "solution"
    return render(request, "index.html", {'obj': name})


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    resad = x + y
    resub=x-y
    remul=x*y
    rediv=x/y
    return render(request, "result.html", {'resad':resad,'resub':resub,'remul':remul,'rediv':rediv})
