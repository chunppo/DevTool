from django.shortcuts import render

def index(request):
    context = {
        'name': 'chunppo'
    }
    return render(request, 'index.html', context);