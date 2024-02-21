from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.contrib import messages
from .models import Animal

def shop(request):
    
    animalss = Animal.objects.all()
    ages = [{'years': animal.age // 12, 'months': animal.age % 12} for animal in animalss]
    animals = [{'id': animal.id, 'image': animal.image, 'name': animal.name, 'breed': animal.get_breed_display(), 'gender': animal.gender, 'years': animal.age // 12, 'months': animal.age % 12} for animal in animalss]

    return render(request, 'main.html', {'animals': animals})

def aboutUs(request):
    return render(request, 'about.html', {})

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Вы вошли в аккаунт."))
            return redirect('main')
        else:
            messages.success(request, ("Произошла ошибка. Попробуйте снова."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта."))
    return redirect('main')
    
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid:
            
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы успешно зарегистрировались."))
            return redirect('main')
        else:
            messages.success(request, ("Произошла ошибка. Попробуйте снова."))
            return redirect('main')
            
    return render(request, 'register.html', {'form':form})

def animal(request, pk):
    animal = Animal.objects.get(id=pk)
    years = animal.age // 12
    months = animal.age % 12

    animal_data = {
        'id': animal.id,
        'image': animal.image,
        'name': animal.name,
        'breed': animal.get_breed_display(),
        'gender': animal.get_gender_display(),
        'years': years,
        'months': months,
        'description': animal.description,
    }

    return render(request, 'animal.html', {'animal': animal_data})
