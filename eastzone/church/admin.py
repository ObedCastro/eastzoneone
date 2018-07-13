from django.contrib import admin
from . models import Region, District, Church

# Register your models here.
class ChurchAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'pastor', 'direction', 'region', 'district',  'created', 'updated')
    list_filter = ['pastor']

admin.site.register(Region)
admin.site.register(District)
admin.site.register(Church, ChurchAdmin)