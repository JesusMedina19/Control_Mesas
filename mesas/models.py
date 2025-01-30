from django.db import models

#Tabla Empleado
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20,default='mesero')

#Tabla Estado
class Estado(models.Model):
    ESTADOS =[
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('en_espera', 'En espera'),

    ]
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10,choices=ESTADOS,default='disponible')

#Tabla Mesa
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero_mesa = models.IntegerField()
    piso = models.IntegerField()
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)