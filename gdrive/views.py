from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .forms import *


def home(request):
    files_o = File.objects.all()
    context = {
        'files': files_o
    }
    return render(request, 'gdrive/home.html', context)


def upload_file(request):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
        files_o = File.objects.all()
        context = {
            'form': form,
            'files': files_o
        }
    return render(request, 'gdrive/upload_file.html', context)


def download_file(request):

    files_o = File.objects.all()
    context = {
        'files': files_o
    }
    return render(request, 'gdrive/download_file.html', context)
