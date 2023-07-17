from __future__ import unicode_literals
from django.db import models


class Register(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Gender = models.TextField(max_length=1, choices=GENDER_CHOICES)
    Date = models.DateField()
    Age = models.IntegerField()
    upload = models.ImageField()

    class Meta:
        db_table = "student"
