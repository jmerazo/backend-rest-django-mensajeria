from rest_framework import serializers
from .models import Empresa, Historial, Estado, Evidencia, Persona, TipoServicio, Planilla, Perfil
from django.contrib.auth.models import User

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
class PersonaSerializer(CurrentUserSerializer):
    class Meta:
        model = Persona
        fields = '__all__'        
class TipoServicioSerializer(CurrentUserSerializer):
    class Meta:
        model = TipoServicio
        fields = '__all__'  
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = (
            'celular'
        )

class UsuarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = '__all__'
class PlanillaSerializer(CurrentUserSerializer):
    class Meta:
        model = Planilla
        fields = '__all__'
