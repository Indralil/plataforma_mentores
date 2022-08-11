import email
from django.db import models

# Create your models here.

class Mentor(models.Model):
    
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=500)
    email = models.EmailField (max_length=100, unique=True)
    ciudad_residencia = models.CharField (max_length=50)
    

    class Meta:
        db_table = 'mentores'

    def __str__(self):
        return self.mentores
