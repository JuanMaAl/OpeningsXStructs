from django.db import models
from django.contrib.auth.models import User

COLOR_SIDE = [
	("White", "White"),
	("Black", "Black"),
]

# Create your models here.

class Repertoires(models.Model):
	repertoire_name = models.CharField(max_length = 30)
	repertoire_color = models.CharField(max_length = 10, choices = COLOR_SIDE, default="White")
	user = models.ForeignKey(User, to_field = "username", on_delete = models.CASCADE, default = "John Doe")
	class Meta:
		unique_together = ('repertoire_name', 'user')
	def __str__(self):
		return self.repertoire_name

class RepertoireVariants(models.Model):
	structure = models.CharField(max_length = 30)
	moves = models.CharField(max_length = 300)
	repertoire_name = models.CharField(max_length = 30)
	user = models.ForeignKey(User, to_field = "username", on_delete = models.CASCADE, default = "John Doe")
	class Meta:
		unique_together = ('moves', 'repertoire_name', 'user')
	def __str__(self):
		return self.moves

class Structures(models.Model):
	structure_name = models.CharField(max_length = 30, unique = True)
	structure_description = models.CharField(max_length = 300)
	def __str__(self):
		return self.structure_name
	
class Variants(models.Model):
	moves = models.CharField(max_length = 300)
	variants_color = models.CharField(max_length = 10, choices = COLOR_SIDE, default="White")
	structures = models.ForeignKey(Structures, to_field = "structure_name", on_delete = models.CASCADE, default = "PDA_1")
	def __str__(self):
		return self.moves
