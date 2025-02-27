from django.db import models
from musician.models import Musician
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, related_name='albums', on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="Rate from 1 to 5")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.album_name

