from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name[0:50]
