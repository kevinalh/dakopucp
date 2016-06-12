from django.db import models

class Keyword (models.Model):
    texto = models.CharField(max_length=30,  unique=True)
    es_hashtag = models.BooleanField()
    es_nombre = models.BooleanField()
    filtro_bool = models.BooleanField(default=True)
    
    def __str__(self):
        return self.texto

class ScrapWeb(models.Model):
    title = models.TextField()
    desc = models.TextField()
    website = models.URLField(max_length=400)
    
    def __str__(self):
        return self.title

class Lugar(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre
        
class Tweet (models.Model):
    # ids del Tweet y del Usuario
    id_tweet = models.CharField(max_length=30)
    id_user = models.CharField(max_length=25,  null=True)
    # Texto del Tweet
    text = models.CharField(max_length=200)
    # Lugar
    location = models.CharField(max_length=50, null=True,  blank=True)
    # El nombre de usuario largo en Twitter
    nombre_usuario = models.CharField(max_length=50,  null=True)
    # El nombre que va con arroba
    screen_name = models.CharField(max_length=25)
    tiempo = models.CharField(max_length=30,  null=True)
    tiempo_real = models.DateTimeField(null = True,  blank=True)
    sentimiento = models.DecimalField(max_digits=6,  decimal_places=5,  null=True)
    mina = models.ForeignKey(Lugar,  null=True,  blank=True)

    def __str__(self):
        return "Tweet: " + self.text
