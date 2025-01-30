from django.db import models

# Tabla Empleado
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=20, default='mesero')

    def __str__(self):
        return self.nombre

# Tabla Estado
class Estado(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('en_espera', 'En espera'),
    ]
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='disponible')

    def __str__(self):
        return self.estado

# Tabla Piso
class Piso(models.Model):
    id_piso = models.AutoField(primary_key=True)
    numero_piso = models.IntegerField()

    def __str__(self):
        return f"Piso {self.numero_piso}"

# Tabla Mesa
class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero_mesa = models.IntegerField()
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE, related_name='mesas')  # Relación corregida
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mesa {self.numero_mesa} - Piso {self.piso.numero_piso}"
