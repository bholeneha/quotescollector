from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'pk': self.id})

class Quote(models.Model):
    quote = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Quote Number {self.id}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id': self.id})

    def new_for_today(self):
        self.discussion_set.filter(date=date.today()).count()

class Discussion(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    thoughts = models.TextField(max_length=2000)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}'s thoughts on quote posted on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for quote_id: {self.quote_id} @{self.url}"