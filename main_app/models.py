from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=100)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.name