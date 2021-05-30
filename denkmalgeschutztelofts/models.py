from django.db import models
from django.utils import timezone


# Create your models here.
class Email(models.Model):
    email = models.CharField(max_length=200, default="not given!")
    created_at = models.DateTimeField(auto_now_add=True)

class Kontakt(models.Model):
    QUELLES = (
        ('KT', 'Kontakt'),
        ('KD', 'Kaiser und Dicke'),
        ('NS', 'Newsletter'),
        ('AN', 'Angebot'),
    )
    email = models.CharField(max_length=200, default="not given!")
    telefon = models.CharField(max_length=200, default="not given!")
    vorname = models.CharField(max_length=200, default="not given!")
    nachname = models.CharField(max_length=200, default="not given!")
    nachricht = models.CharField(max_length=200, default="kein nachricht")
    created_at = models.DateTimeField(auto_now_add=True)
    quelle = models.CharField(max_length=2, choices=QUELLES, default="KT")


