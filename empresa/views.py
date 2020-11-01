
from rest_framework import viewsets
from .serializers import EmpresaSerializer, HistorialSerializer, EstadoSerializer, EvidenciaSerializer, TercerosSerializer, TipoServicioSerializer, Empresa, Historial, Estado, Evidencia, Terceros, TipoServicio
from rest_framework.permissions import IsAuthenticated


class CurrentUser(viewsets.ModelViewSet):
 
    def get_queryset(self):
      user = self.request.user 
      return self.serializer_class.Meta.model.objects.filter(usuario=user)

      
class EmpresaView(CurrentUser):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]  

class HistorialView(CurrentUser):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
    permission_classes = [IsAuthenticated]  
class EstadoView( CurrentUser):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [IsAuthenticated]  
class EvidenciaView( CurrentUser):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
    permission_classes = [IsAuthenticated]  

class TercerosView( CurrentUser):
    queryset = Terceros.objects.all()
    serializer_class = TercerosSerializer
    permission_classes = [IsAuthenticated]  
class TipoServicioView( CurrentUser):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
    permission_classes = [IsAuthenticated]  

#ala madre tengo reclado ingles