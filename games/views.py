from django.shortcuts import render
from .models import Game


def index(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games/index.html', context)
