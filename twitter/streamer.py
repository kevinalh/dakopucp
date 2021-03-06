from twitter.models import Tweet,  Keyword

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import OperationalError,  connection

from unidecode import unidecode
import tweepy
import time

class Command(BaseCommand):
    help = "Corre el comando que leera los tweets y los guardara en la base de datos"

    def handle(self, *args, **options):
        class StreamListenerMineria(tweepy.StreamListener):

            def on_status(self, status):
                id_twitter =  status.id_str
                id_usuario = status.user.id_sttr
                texto =  unidecode(status.text)
                lugar =  status.location
                username = status.user.location
                screename = status.user.screen_name
                tweet = Tweet.objects.create(id_str = id_twitter,  id_user = id_usuario,  text = texto, 
                location = lugar,  nombre_usuario = username,  screen_name = screename)
                tweet.save()

                def on_error(self, status):
                    if status == 420:
                        return False
                    else:
                        return True

        auth = tweepy.OAuthHandler(settings.CONSUMER_TOKEN, settings.CONSUMER_SECRET)
        api = tweepy.API(auth)

        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)

        myStreamMineria = StreamListenerMineria()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamMineria)

        keywords = Keyword.objects.all()
        keywords_filtro = keywords.filter(filtro_bool = True)

        tracklist = [keyword.texto for keyword in keywords_filtro]

        def obtenertweets():
            try:
                myStream.filter(track=tracklist, languages=['es'])
            except OperationalError:
                print("Operational Error!")
                connection.connection.close()
                connection.connection = None
                time.sleep(6)
                return obtenertweets()

        if __name__ == 'twitstream.management.commands.obtenertweets':
            try:
                obtenertweets()
            except KeyboardInterrupt:
                print("Cancelado por teclado")
