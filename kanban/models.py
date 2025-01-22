from django.db import models

class Prospect(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=50, choices=[
        ('fase1', 'Fase 1'),
        ('fase2', 'Fase 2'),
        ('fase3', 'Fase 3'),
        ('fase4', 'Fase 4')
    ], default='fase1')

    def __str__(self):
        return self.name
