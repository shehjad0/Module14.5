from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    return render(request, 'app/index.html')