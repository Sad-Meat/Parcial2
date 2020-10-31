from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto      = models.AutoField(db_column='id_producto', primary_key=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    precio           = models.CharField(max_length=40, blank=True, null=True)
    fecha_env = models.DateField(blank=True, null=True)
    marca            = models.CharField(max_length=40, blank=True, null=True)
    imagen           = models.ImageField(upload_to='imagenes', blank=True, null=True)






    def __str__(self):

        return self.nombre + ", " + self.precio + ", " \
               + str(self.fecha_env) + ", " \
               + self.marca + ", " + self.imagen.__str__()
    class Meta:
        ordering =["id_producto"]