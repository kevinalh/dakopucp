from django.db import models

class Tweet (models.Model):
    # ids del Tweet y del Usuario
    id_tweet = models.CharField(max_length=30)
    id_user = models.CharField(max_length=25)
    # Texto del Tweet
    text = models.CharField(max_length=200)
    # Lugar
    location = models.CharField(max_length=50, null=True,  blank=True)
    # El nombre de usuario largo en Twitter
    nombre_usuario = models.CharField(max_length=50)
    # El nombre que va con arroba
    screen_name = models.CharField(max_length=25)

    def __str__(self):
        return "Tweet: " + self.text

class Keyword (models.Model):
    texto = models.CharField(max_length=30,  unique=True)
    es_hashtag = models.BooleanField()
    es_nombre = models.BooleanField()
    filtro_bool = models.BooleanField(default=True)
    
    def __str__(self):
        return self.texto
