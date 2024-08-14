from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def to_home(request):
    return redirect('home')