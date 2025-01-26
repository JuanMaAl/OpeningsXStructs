from django.http import HttpResponse
from django.shortcuts import render
from .models import Repertoires, Structures, Variants, RepertoireVariants
from .create_rep import new_repertoire, process_new_repertoire
from .delete_rep import delete_repertoire, process_delete_repertoire
from .open_rep import open_repertoire
from .add_to_rep import add_to_repertoire
from .del_from_rep import del_from_repertoire
from .login import login_user

# Create your views here.

def home(request):
	user_name = request.user
	repertoires = Repertoires.objects.filter(user = user_name)
	context = {
		'user_name' : user_name,
		'repertoires' : repertoires
	}
	return render(request, 'home.html', context)

def structures(request, repertoire_name, repertoire_color):
	structures = Structures.objects.all()
	user = request.user
	context = {
		'user' : user,
		'repertoire_name' : repertoire_name,
		'repertoire_color' : repertoire_color,
		'structures' : structures
	}
	return render(request, 'structures.html', context)

def variants(request, repertoire_name, repertoire_color, 
structure_name):
	variants = Variants.objects.filter(structures = structure_name, variants_color = repertoire_color)
	user = request.user
	context = {
		'structure' : structure_name,
		'variants' : variants,
		'repertoire_name' : repertoire_name,
		'user_id' : user,
		'repertoire_color' : repertoire_color
	}
	return render(request, 'variants.html', context)
