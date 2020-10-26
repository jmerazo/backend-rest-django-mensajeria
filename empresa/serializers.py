from rest_framework import serializers
from .models import Empresa, Historial, Estado, Evidencia, Terceros, TipoServicio

class CurrentUserSerializer(serializers.ModelSerializer):
     usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

class EmpresaSerializer(CurrentUserSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        
class HistorialSerializer(CurrentUserSerializer):
    class Meta:
        model = Historial
        fields = '__all__'        
class EstadoSerializer(CurrentUserSerializer):
    class Meta:
        model = Estado
        fields = '__all__'        
class EvidenciaSerializer(CurrentUserSerializer):
    class Meta:
        model = Evidencia
        fields = '__all__'       
class TercerosSerializer(CurrentUserSerializer):
    class Meta:
        model = Terceros
        fields = '__all__'        
class TipoServicioSerializer(CurrentUserSerializer):
    class Meta:
        model = TipoServicio
        fields = '__all__'  