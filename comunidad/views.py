from django.shortcuts import render

from rest_framework import generics

from comunidad.models import Comunidad, Miembro
from comunidad.serializers import ComunidadSerializer, MiembroSerializer


class ComunidadList(generics.ListCreateAPIView):
	queryset = Comunidad.objects.all()
	serializer_class = ComunidadSerializer


class ComunidadDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comunidad.objects.all()
	serializer_class = ComunidadSerializer


class MiembroList(generics.ListCreateAPIView):
	queryset = Miembro.objects.all()
	serializer_class = MiembroSerializer


class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Miembro.objects.all()
	serializer_class = MiembroSerializer

