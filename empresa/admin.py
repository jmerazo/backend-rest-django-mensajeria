from django.contrib import admin
from .models import Historial, Terceros, Estado, Empresa, Evidencia,Planilla

# Register your models here.
class TercerosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Terceros, TercerosAdmin)

class EstadoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Estado, EstadoAdmin)
class EmpresaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Empresa, EmpresaAdmin)
class HistorialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Historial, HistorialAdmin)
class EvidenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Evidencia, EvidenciaAdmin)
class PlanillaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Planilla, PlanillaAdmin)