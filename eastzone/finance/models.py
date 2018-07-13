from django.db import models
from church.models import Region, Church, District

# Create your models here.
class Finance(models.Model):
    code = models.CharField(max_length=6, verbose_name="Código")
    name_church = models.ForeignKey(Church, verbose_name="Nombre de iglesia", on_delete=models.CASCADE)
    region = models.ForeignKey(Region, verbose_name="Region", on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name="Dirstrito", on_delete=models.CASCADE)
    reports = models.CharField(max_length=100, verbose_name="Quien reporta")
    POSITION = (
        ('P', 'Presidente'),
        ('V', 'Vice_presidente'),
        ('S', 'Secretario'),
        ('T', 'Tesorero'),
        ('M', 'Miembro'),
    )
    position = models.CharField(max_length=12, choices=POSITION, default='M', blank=True, verbose_name="Cargo")
    MESES = (
        ('ENERO', 'ENERO'),
        ('FEBRERO', 'FEBRERO'),
        ('MARZO', 'MARZO'),
        ('ABRIL', 'ABRIL'),
        ('MAYO', 'MAYO'),
        ('JUNIO', 'JUNIO'),
        ('JULIO', 'JULIO'),
        ('AGOSTO', 'AGOSTO'),
        ('SEPTIEMBRE', 'SEPTIEMBRE'),
        ('OCTUBRE', 'OCTUBRE'),
        ('NOVIEMBRE', 'NOVIEMBRE'),
        ('DICIEMBRE', 'DICIEMBRE'),
    )
    month = models.CharField(max_length=12, choices=MESES, blank=True, default='M', verbose_name="Mes")
    CATEGORIA = (
        ('Diezmos', 'Diezmos'),
        ('Ofrendas', 'Ofrendas'),
    )
    category = models.CharField(max_length=12, choices=CATEGORIA, blank=True, default='Ofrendas', verbose_name="Categoría")
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cantidad $ ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Finanzas"
        verbose_name_plural = "Finanzas"
        ordering = ['month']
        
    def __str__(self):
        return self.code