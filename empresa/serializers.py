from rest_framework import serializers
from .models import Empresa, Historial, Estado, Evidencia, Persona, TipoServicio, Planilla, Perfil, Guia
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
     usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

class EmpresaSerializer(CurrentUserSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        
class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'

class EstadoSerializer(CurrentUserSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class EvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencia
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
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

class PlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planilla
        fields = '__all__'

class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'
