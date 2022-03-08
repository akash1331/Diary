from tabnanny import verbose
from django.db import models
from django.db.models.deletion import SET_NULL
from pandas import notnull

# Create your models here.
class diaryModel(models.Model):
    text=models.CharField(max_length=100)
    datesave= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Entries'