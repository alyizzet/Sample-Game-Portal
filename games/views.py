from django.shortcuts import render
from django.http import HttpResponse
from .models import Game


def homepage(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'homepage.html', context)
