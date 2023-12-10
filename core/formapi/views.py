from django.shortcuts import render
from .forms import customForm

# Create your views here.

def index(request):
    return render(request, 'formapi/index.html')

def formapi(request):
    form = customForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'formapi/index.html', {'form':form})