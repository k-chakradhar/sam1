from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=50)
    u_pass1 = models.CharField(max_length=50)
    u_pass2 = models.CharField(max_length=50)