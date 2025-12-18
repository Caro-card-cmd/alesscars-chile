from django.db import models

class agenda(models.Model):
    # Opciones fijas de servicios (las mismas que en tu HTML <select>)
    SERVICIOS = [
        ('Sellado', 'Sellado de Cerámico'),
        ('Pulido', 'Pulido Profesional'),
        ('Pintura', 'Pintura de Carrocería'),
        ('Desabolladura', 'Desabolladura'),
        ('Lavado', 'Lavado Completo'),
        ('RestauracionFocos', 'Restauración de Focos'),
        ('LavadoMotor', 'Lavado de Motor'),
        ('Sanitizado', 'Sanitizado con Ozono'),
        ('Tapiceria', 'Lavado de Tapiz'),
    ]

    id = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=50, choices=SERVICIOS)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True)

    def __str__(self):
        return f"{self.servicio} - {self.marca} {self.modelo}"

    def delete(self, using=None, keep_parents=False):
        # elimina la imagen del sistema cuando se borra un registro
        if self.imagen:
            self.imagen.storage.delete(self.imagen.name)
        super().delete()
