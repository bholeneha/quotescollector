from django.db import models
from django.urls import reverse

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'Quote Number {self.id}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id': self.id})