from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name[0:50]
