from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.order_by('-date')
    context = {'notes' : notes}
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    context = {'form' : form}

    return render(request, 'add.html', context)