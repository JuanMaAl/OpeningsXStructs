from django.db import models

COLOR_SIDE = [
	("White", "White"),
	("Black", "Black"),
]

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	def __str__(self):
		return self.name

class Repertoires(models.Model):
	repertoire_name = models.CharField(max_length = 30)
	repertoire_color = models.CharField(max_length = 10, choices = COLOR_SIDE, default="White")
	user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
	def __str__(self):
		return self.repertoire_name

class RepertoireVariants(models.Model):
	structure = models.CharField(max_length = 30)
	moves = models.CharField(max_length = 300)
	repertoires = models.ManyToManyField(Repertoires)
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
