from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=25, verbose_name="Región")
    
    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ['name']
        
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50, verbose_name="Distrito")
    
    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Church(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de iglesia")
    pastor = models.CharField(max_length=100, verbose_name="Pastor")
    region = models.ForeignKey(Region, verbose_name="Región", on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name="Distrito", on_delete=models.CASCADE)
    direction = models.CharField(max_length=500, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Iglesia"
        verbose_name_plural = "Iglesias"
        ordering = ['created']
        
    def __str__(self):
        return self.name