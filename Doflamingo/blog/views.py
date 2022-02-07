from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'blog/Home.html')

def matplotib(request):
    return render(request, 'blog/About-pages/Matplotib.html')

def panda(request):
    return render(request, 'blog/About-pages/Panda.html')

def request(request):
    return render(request, 'blog/About-pages/Request.html')

def flask(request):
    return render(request, 'blog/About-pages/Flask.html')

def django(request):
    return render(request, 'blog/About-pages/Django.html')

def numpy(request):
    return render(request, 'blog/About-pages/Numpy.html')

def beautifullsoup(request):
    return render(request, 'blog/About-pages/Beautifullsoup.html')

def tester(request):
    return render(request, 'blog/About-pages/Tester.html')