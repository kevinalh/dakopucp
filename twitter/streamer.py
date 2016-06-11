from .models import Tweet

import settings
import unidecode
import tweepy

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

