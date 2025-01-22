from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires, Structures, Variants, RepertoireVariants
from .create_rep import new_repertoire, process_new_repertoire
from .delete_rep import delete_repertoire, process_delete_repertoire

# Create your views here.

def home(request, user_name):
	user = User.objects.filter(name = user_name)
	repertoires = Repertoires.objects.filter(user = user_name)
	return render(request, 'home.html', 
	{'user': user, 'repertoires': repertoires})

def structures(request):
	structures = Structures.objects.all()
	return render(request, 'structures.html', {'structures': structures})

def variants(request, structure_name):
	variants = Variants.objects.filter(structures = structure_name)
	return render(request, 'variants.html', {'variants': variants})

def open_repertoire(request, user, repertoire_name):
	try:
		variants = RepertoireVariants.objects.filter(user_id=user, repertoire_name = repertoire_name)
	except RepertoireVariants.DoesNotExist:
		variants = []
	return render(request, 'open_repertoire.html', {'variants': variants})
