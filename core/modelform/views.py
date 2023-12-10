from django.shortcuts import render, redirect
from . import models
from .forms import CustomForm

# Create your views here.

def index(request):
    return render(request, 'modelform/index.html')

def model_form(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("modelform")
    else:
        form = CustomForm()
            
    data = models.CustomModel.objects.all()
    
    return render(request, 'modelform/index.html', { "form": form, "data": data })