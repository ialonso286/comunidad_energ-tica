from rest_framework import serializers
from comunidad.models import Comunidad, Miembro



class ComunidadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comunidad
		fields = ('id', 'nombre', 'descripcion', 'latitud', 'longitud')


class MiembroSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Miembro
		fields = ('id','nif','nombre','der', 'latitud', 'longitud')
