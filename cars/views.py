from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def landing(request):
    if request.method == "POST":
        query = request.POST.get('query', None)
        results = Car.objects.filter(color=query)
        return render(request, 'landing.html', {'cars':results})
    return render(request, 'landing.html')

def update_car(request, pk):
    car = Car.objects.get(name=pk)
    form = update_CarForm(instance=car)
    if request.method == 'POST':
        form = update_CarForm(request.POST, instance = car)
        if form.is_valid():
            form.save()
            return redirect("landing")
    return render(request, "add_car.html", {'form':form})

def delete_car(request, pk):
    Car.objects.get(pk=pk).delete()
    return redirect('landing')

def add_car(request):
    form = add_CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("landing")
    return render(request, "add_car.html", {'form':form})