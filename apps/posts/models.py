from django.db import models

class Ods(models.Model):
	nombre= models.CharField(max_length = 30)
	descripcion= models.CharField(max_length = 100, null = False)
	imagen= models.ImageField(upload_to='imagenes_ods', null=True)

	def __str__(self):
		return self.nombre

class Posts(models.Model):
	Titulo= models.CharField(max_length = 30)
	descripcion= models.CharField(max_length = 100, null = False)
	Ods=models.ForeignKey(Ods, on_delete = models.CASCADE)
	imagen= models.ImageField(upload_to='imagenes_posts', null=True)



	def __str__(self):
		return self.Titulo
