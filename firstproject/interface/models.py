from django.db import models
from django.db.models.fields import CharField

class addusers(models.Model):
    username=models.CharField(max_length=100) 
    email=models.EmailField(max_length=100,unique=True, primary_key=True) 
    password=models.CharField(max_length=100) 

    class Meta:
        ordering = ["email"]

    def __str__(self) -> str:
        return f'{self.email}'

    