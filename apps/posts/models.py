from django.db import models

class Ods(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.TextField(null = True)
	imagen = models.ImageField(upload_to='imagenes_ods', null=True)

	def __str__(self):
		return self.nombre

class Posts(models.Model):
	nombre = models.CharField(max_length=255)
	body = models.TextField(null = True)
	fecha_post = models.DateTimeField(auto_now_add=True, null = True)
	Ods = models.ForeignKey(Ods, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to='imagenes_posts', null=True)
		
	class Meta:
		ordering = ['-fecha_post']

	def __str__(self):
		return self.nombre
