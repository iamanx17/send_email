from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class emailids(models.Model):
    email=models.EmailField(max_length=250)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)
    user=models.ForeignKey(User,  on_delete=models.CASCADE)

    class Meta:
        ordering:['date']
        verbose_name='Email id'

    def __str__(self):
        return self.email

