from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title           = models.CharField(max_length=100)
    author          = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    status          = models.BooleanField(default=False)
    user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title