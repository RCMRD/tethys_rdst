from django.shortcuts import render, reverse
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    app_button = Button (
        display_text = "Launch App",
        name = 'launch_app',
        style='success',
        href=reverse('rdst:app')
        )

    context = {
    'launch_app': app_button
    }
    return render(request, 'rdst/home.html', context)

def app(request):
    context = {
    }

    return render(request, 'rdst/app.html', context)

def login(request):
    context = {
    }

    return render(request, 'rdst/login.html', context)