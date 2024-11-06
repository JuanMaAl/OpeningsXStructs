from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	def __str__(self):
		return self.name

class Repertoires(models.Model):
	repertoire_name = models.CharField(max_length = 30)
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
	structures = models.ForeignKey(Structures, on_delete = models.CASCADE, default = 1)
	def __str__(self):
		return self.moves
