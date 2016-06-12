# -*- coding: utf-8 -*-
from twitter.models import Tweet,  Lugar

from django.core.management.base import BaseCommand
# from django.db.models import Q
from django.conf import settings

from tqdm import tqdm
import indicoio
import time
from decimal import Decimal

class Command(BaseCommand):
    help = "Corre el programa de analisis de sentimiento y lugares para Tweets"
    def handle(self,  *args, **options):
        def correr():
            indicoio.config.api_key = settings.KEY_INDICOIO

            while(1):
                # En un principio fue necesario usar objetos Q para usar or, pero ya no lo es pues se modifico el codigo para que se haga el analisis de sentimiento
                # y de localizacion a la vez
                # tweets = Tweet.objects.filter(Q(sentimiento=None) | Q(mina=None))
                tweets = Tweet.objects.filter(sentimiento=None)

                for tweet in  tqdm(tweets):
                    sent = indicoio.sentiment_hq(tweet.text)
                    tweet.sentimiento = Decimal(sent)
                    lugares = Lugar.objects.all()
                    for lugar in  lugares:
                        # Autocritica: Se puede evitar el bucle for aprovechando los QuerySets de Django. Mucho mas veloces.
                        if lugar.nombre in tweet.text:
                            # Obviamente si hay mas de un lugar, se va a quedar con el ultimo. Este caso no se considerara por ser prototipo de Hackaton
                            tweet.mina = lugar
                    tweet.save()
                
                time.sleep(10)
                
        try:
            correr()
        except KeyboardInterrupt:
            print("Cancelado por teclado")
