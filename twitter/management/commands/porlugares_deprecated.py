# -*- coding: utf-8 -*-
# OBSOLETO
from twitter.models import Tweet,  Lugar
from tqdm import tqdm

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Clasifica Tweets por lugares"

    def handle(self, *args, **options):
        
        def clasificar():
            tweets = Tweet.objects.all()
            lugares = Lugar.objects.all()
            for tweet in tqdm(tweets):
                for lugar in  lugares:
                    # Autocritica: Se puede evitar el bucle for aprovechando los QuerySets de Django. Mucho mas veloces.
                    if lugar.nombre in tweet.text:
                        # Obviamente si hay mas de un lugar, se va a quedar con el ultimo. Este caso no se considerara por ser prototipo de Hackaton
                        tweet.mina = lugar
                        tweet.save()
        try:
            clasificar()
        except KeyboardInterrupt:
            print("Cancelado por teclado")
