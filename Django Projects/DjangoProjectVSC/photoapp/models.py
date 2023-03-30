from django.db import models

# Create your models here.


class Photo(models.Model):

    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-' + self.creator
