from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {}) #about contact cursos

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def curso(request):
    return render(request, 'cursos.html', {})