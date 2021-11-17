from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Deck: {self.name}'