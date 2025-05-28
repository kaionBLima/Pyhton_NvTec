from django.shortcuts import render
from .models import todo

def home(request):
    todos = todo.objects.all()
    return render(request, 'home.html', {})

def about(request):
    context = {'name': 'John Dow', 'age': 30}
    return render(request, 'about.html', context)
