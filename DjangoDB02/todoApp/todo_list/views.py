from django.shortcuts import render
from django.contrib import messages
from .models import todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo adicionado com sucesso!')
    else:
        form = TodoForm()  # instância vazia para exibir no template

    todos = todo.objects.all()
    return render(request, 'home.html', {'todos': todos, 'form': form})


def about(request):
    context = {'name': 'John Dow', 'age': 30}
    return render(request, 'about.html', context)
