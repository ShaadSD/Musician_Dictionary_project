from django.db import models

class Musician(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Number=models.CharField(max_length=11)
    Instrument=models.CharField(max_length=100)

    def __str__(self):
        return self.First_name