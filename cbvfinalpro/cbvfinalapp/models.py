from django.db import models
from django.urls import reverse


class Beer(models.Model):
    name = models.CharField(max_length=50)
    teste = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

