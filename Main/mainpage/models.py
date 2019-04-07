from django.db import models
from .custom.PointFileStorage import PointFileStorage
# Create your models here.

mfs = PointFileStorage() # PointFileStorage do not create the copy of files when storing it

class wordEntry(models.Model):
    word = models.CharField(max_length=200)
    gondiFile = models.FileField(null=True)
    pId = models.IntegerField()