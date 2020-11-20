from django.urls import path
from .views import EmpresaView, HistorialView, EstadoView, EvidenciaView, TercerosView, TipoServicioView, UsuariosView,PlanillaView,PlanillaMensajeroView,Historico,HistoricoView

urlpatterns = [
    path('empresa/',EmpresaView.as_view({
        'get' : 'list',
        'post' : 'create',
        'delete': 'destroy',
        'put': 'update',      

    })),
    path('empresa/<int:pk>', EmpresaView.as_view({
        'get':'retrieve',
        'put': 'update',
        'post': 'create',
        'delete': 'destroy',

    })),

    path('historial/',HistorialView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),

     path('historial/<int:pk>', HistorialView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })),
    path('estado/',EstadoView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('estado/<int:pk>', EstadoView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })),
    path('evidencia/', EvidenciaView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('evidencia/<int:pk>', EvidenciaView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })),
    path('terceros/',TercerosView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('terceros/<int:pk>', TercerosView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })), 
    path('tiposervicio/',TipoServicioView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('tiposervicio/<int:pk>', TipoServicioView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })), 
    path('usuarios', UsuariosView.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
    })),      
    path('usuarios/<int:pk>', UsuariosView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('planilla/',PlanillaView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('planilla/<int:pk>', PlanillaView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),    
    path('planillamensajero/',PlanillaMensajeroView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('planillamensajero/<int:pk>', PlanillaMensajeroView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
     path('historico/',HistoricoView.as_view({
        'get' : 'list',
        'post' : 'create',        

    })),
    path('historico/<int:pk>', HistoricoView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),                 

]