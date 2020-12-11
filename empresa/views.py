
from rest_framework import viewsets
from .serializers import EmpresaSerializer, HistorialSerializer, EstadoSerializer, EvidenciaSerializer, PersonaSerializer, TipoServicioSerializer, Empresa, Historial, Estado, Evidencia, Persona, TipoServicio, UsuarioSerializer, User,Planilla,PlanillaSerializer, Guia, GuiaSerializer
from rest_framework.permissions import IsAuthenticated


class CurrentUser(viewsets.ModelViewSet):
 
    def get_queryset(self):
      user = self.request.user 
      return self.serializer_class.Meta.model.objects.filter(usuario=user)

      
class EmpresaView(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]  

class HistorialView(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer

class EstadoView(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
  
class EvidenciaView(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer

class PersonaView(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nombres', 'id']
class TipoServicioView(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
    permission_classes = [IsAuthenticated]

class UsuariosView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
class PlanillaView(viewsets.ModelViewSet):
    queryset = Planilla.objects.all()
    serializer_class = PlanillaSerializer

class GuiaView(viewsets.ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer
    search_fields = ['id', 'numero']

    
