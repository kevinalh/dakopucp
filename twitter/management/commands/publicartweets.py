# -*- coding: utf-8 -*-
from twitter.models import Tweet

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Avg

import tweepy
import time
import datetime

class Command(BaseCommand):
    help = "Corre el comando que leera los tweets y los guardara en la base de datos"

    def handle(self, *args, **options):
        auth = tweepy.OAuthHandler(settings.CONSUMER_TOKEN, settings.CONSUMER_SECRET)
        api = tweepy.API(auth)

        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)

        def publicartweets():
            while(1):
                seguir=1
                # El contador de python no gasta una cantidad significativa de tiempo
                cantidad = Tweet.objects.all().count()
                tiempo_inicio = datetime.datetime.now() - datetime.timedelta(minutes=1)
                # TODO: Mas elegancia con breaks
                while(seguir):
                    time.sleep(30)  # Para el demo, lo dejamos en 30. Normalmente podria ser una hora o mas para evitar el spam
                    print("-")  # Sanity check
                    cantidad2= Tweet.objects.all().count()
                    resta = cantidad2 - cantidad  # Cuanto ha cambiado la cantidad de tweets con respecto al comienzo del bucle
                    if resta > 1:
                        publicacion = "#Prueba "
                        sentimiento = Tweet.objects.filter(tiempo_real__gt=tiempo_inicio).exclude(sentimiento=None).aggregate(Avg('sentimiento'))
                        sent = float('%.3f'%(sentimiento['sentimiento__avg']))
                        if sent > 0.6:
                            texto = "Sentimiento favorable"
                        elif sent > 0.4:
                            texto = "Sentimiento neutral"
                        else:
                            texto = "Sentimiento desfavorable"
                        publicacion = publicacion + texto + ". En promedio: " + str(sent)
                        api.update_status(publicacion)  # Se publica el tweet luego de sacar el promedio de los tweets de los ultimos minutos
                        print("Publicado")
                        seguir=0
                    else:
                        seguir=1
                

        try:
            publicartweets()
        except KeyboardInterrupt:
            print("Cancelado por teclado")
