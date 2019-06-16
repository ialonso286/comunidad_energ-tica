from django.db import models

class Comunidad(models.Model):
	nombre = models.CharField(max_length = 100, unique = True)
	descripcion = models.TextField()
	latitud = models.FloatField()
	longitud = models.FloatField()


class Miembro(models.Model):
	nif = models.CharField(max_length = 10, unique = True)
	nombre = models.CharField(max_length = 100, unique = True)
	der = models.CharField(max_length = 100, unique = True)
	latitud = models.FloatField()
	longitud = models.FloatField()
	comunidad = models.ForeignKey('Comunidad', on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		



	    super().save(*args, **kwargs)

