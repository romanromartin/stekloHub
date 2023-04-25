from django.db import models



class Peregorodki(models.Model):
    picture = models.ImageField(upload_to='static/media/peregorodki', default='static/media/peregorodki/default.webp')


class Kozirki(models.Model):
    picture = models.ImageField(upload_to='static/media/kozirki', default='static/media/kozirki/default.webp')


class Nerjograda(models.Model):
    picture = models.ImageField(upload_to='static/media/nerjograda', default='static/media/nerjograda/default.webp')


class Stekloograda(models.Model):
    picture = models.ImageField(upload_to='static/media/stekloograda', default='static/media/stekloograda/default.webp')

class Interer(models.Model):
    picture = models.ImageField(upload_to='static/media/interer', default='static/media/interer/default.webp')


