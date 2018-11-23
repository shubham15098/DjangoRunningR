from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Try(models.Model):
    checkIt = models.IntegerField(null = True)
    minCells = models.IntegerField(null = True)
    minGenes = models.IntegerField(null = True)
    # minGenes = models.IntegerField()