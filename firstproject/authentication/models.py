from django.db import models
from datetime import datetime
from interface.models import addusers

class addblog(models.Model):
    author = models.ForeignKey(to=addusers , on_delete =models.CASCADE)
    tittle = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.author}"