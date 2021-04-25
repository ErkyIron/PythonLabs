from django.shortcuts import render
from embedded_systems.forms import CommandForm
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
import os

def embedded_systems_index(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            with open(os.path.join(settings.BASE_DIR, 'embedded_systems\commands.txt'), 'a') as file:
                file.write(form.cleaned_data['body'] + '\n')


    with open(os.path.join(settings.BASE_DIR, 'embedded_systems\commands.txt'), 'r') as file:
        lines = file.readlines()

    form = CommandForm()

    context = {
        'form': form,
        'lines' : lines,
    }

    return render(request, 'embedded_systems_index.html', context)

def clear_commands(request):
    with open(os.path.join(settings.BASE_DIR, 'embedded_systems\commands.txt'), 'a') as file:
        file.truncate(0)

    return HttpResponseRedirect(reverse('embedded_systems_index'))
