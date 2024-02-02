from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'splash.html')

def signup1(request):
    return render(request, 'signup1.html')

def signup2(request):
    return render(request, 'signup2.html')

def bookselect(request):
    return render(request, 'bookselect.html')

def genreselect(request):
    return render(request, 'genreselect.html')

def authorselect(request):
    return render(request, 'authorselect.html')

def underselection(request):
    return render(request, 'underselection.html')