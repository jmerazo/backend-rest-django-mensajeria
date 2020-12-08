from django.contrib import admin
from .models import Historial, Persona, Estado, Empresa, Evidencia, Planilla, TipoServicio, Guia

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Persona, PersonaAdmin)

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
class TipoServicioAdmin(admin.ModelAdmin):
    pass
admin.site.register(TipoServicio, TipoServicioAdmin)
class GuiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Guia, GuiaAdmin)
