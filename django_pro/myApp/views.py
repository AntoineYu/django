from django.shortcuts import render
#from django.views import View
from django.http import HttpResponse

# Create your views here.
def get(request):
    return render(request,'registrer.html')

def log(request):
    return render(request,'login.html')