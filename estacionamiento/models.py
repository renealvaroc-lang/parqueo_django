from django.db import models
from django.core.exceptions import ValidationError


# CLIENTE

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# VEHICULO

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.placa

# ESPACIO

class Espacio(models.Model):
    numero = models.IntegerField()
    estado = models.CharField(max_length=20, default='libre')

    def __str__(self):
        return f"Espacio {self.numero}"

# REGISTRO

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)

    estado = models.CharField(max_length=20, default='activo')
    costo = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def clean(self):
        #Espacio ocupado
        if self.estado == 'activo' and self.espacio:
            existe = Registro.objects.filter(
                espacio=self.espacio,
                estado='activo',
                fecha_salida__isnull=True
            ).exclude(id=self.id).exists()

            if existe:
                raise ValidationError("Este espacio ya está ocupado.")

        #Vehículo duplicado
        if self.estado == 'activo' and self.vehiculo:
            existe = Registro.objects.filter(
                vehiculo=self.vehiculo,
                estado='activo',
                fecha_salida__isnull=True
            ).exclude(id=self.id).exists()

            if existe:
                raise ValidationError("Este vehículo ya está dentro del parqueo.")

        #Validación de fechas
        if self.fecha_salida and self.fecha_ingreso:
            if self.fecha_salida < self.fecha_ingreso:
                raise ValidationError("La fecha de salida no puede ser menor a la de ingreso.")

    def save(self, *args, **kwargs):
        self.clean()

        es_nuevo = self.pk is None

        super().save(*args, **kwargs)

        #Cuando entra (nuevo registro)
        if es_nuevo:
            self.espacio.estado = 'ocupado'
            self.espacio.save()

        #Cuando sale
        if self.fecha_salida:
            self.estado = 'finalizado'

            tiempo = self.fecha_salida - self.fecha_ingreso
            horas = tiempo.total_seconds() / 3600

            tarifa = 5  # Bs por hora
            self.costo = round(horas * tarifa, 2)

            self.espacio.estado = 'libre'
            self.espacio.save()

            super().save(update_fields=['estado', 'costo'])

    def __str__(self):
        return f"{self.vehiculo} - {self.estado}"
