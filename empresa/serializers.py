from rest_framework import serializers
from .models import Empresa, Historial, Estado, Evidencia, Persona, TipoServicio, Planilla, Perfil, Guia
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
     usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

class EmpresaSerializer(serializers.ModelSerializer):
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

class PersonaSerializer(serializers.ModelSerializer):
    """ guia = GuiaSerializer(many=True, read_only=False)
    evidencia = EvidenciaSerializer(many=True, read_only=False)
    historial = HistorialSerializer(many=True, read_only=False) """

    class Meta:
        model = Persona
        fields = (
            'id',
            'nombres',
            'apellidos',
            'celular',
            'whatsapp',
            'correo',
            'direccion',
            'ciudad',
            'departamento',
        )

    """ def create(self, validated_data):
        # Crear persona
        persona = Persona.objects.create(
            nombres = validated_data['nombres'],
            apellidos = validated_data['apellidos'],
            celular = validated_data['celular'],
            whatsapp = validated_data['whatsapp'],
            correo = validated_data['correo'],
            direccion = validated_data['direccion'],
            ciudad = validated_data['ciudad'],
            departamento = validated_data['departamento'],
        )

        guia = validated_data.pop('guia')
        guia.objects.create(
            persona=Persona,
            numero=guia['numero'],
            persona_g=guia['persona_g'],
        )

        evidencia = validated_data.pop('evidencia')
        evidencia.objects.create(
            persona=Persona,
            nombre=evidencia['nombre'],
            imagen=evidencia['imagen'],
            persona_e=evidencia['persona_e'],
        )

        historial = validated_data.pop('historial')
        historial.objects.create(
            persona=Persona,
            nombre=historial['nombre'],
            persona_h=historial['persona_h'],
        ) """
        
