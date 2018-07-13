from django.contrib import admin
from django.db.models import Sum
from . models import Finance
from church.models import Region, District, Church

# Register your models here.
class FinanceAdmin(admin.ModelAdmin):  
    #Función para mostrar el la suma de la columna 'amount'
    def changelist_view(self, request, extra_context=None):
        total = Finance.objects.aggregate(total=Sum('amount'))['total']
        context = {
            'total': total,
        }
        return super(FinanceAdmin, self).changelist_view(request, extra_context=context)

    
    readonly_fields = ('created', 'updated') #No permitir edición
    list_display = ('code', 'month', 'name_church', 'region', 'district', 'category', 'amount', 'reports', 'position', 'created', 'updated') #Campos a mostrar
    search_fields = ['code', 'month', 'category', 'name_church__name'] #Búsqueda por mes
    list_filter = ['region__name', 'district__name', 'name_church__name', 'month']

admin.site.register(Finance, FinanceAdmin)