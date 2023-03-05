from django.db import models

# Create your models here.
class Actividades(models.Model):
    nombre_de_actividad=models.CharField(max_length=30)
    sector_asignado=models.CharField(max_length=20)
    objetivo=models.CharField(max_length=100)
    monto_planificado=models.IntegerField()
    periodo=models.DateTimeField()
    
    def __str__(self):
        return '{}'.format(self.nombre_de_actividad)