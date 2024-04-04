from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Event(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name