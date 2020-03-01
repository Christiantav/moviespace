from django.db import models

# Create your models here.
class User(models.Model):
   	 email = models.TextField()
   	 name = models.TextField()
