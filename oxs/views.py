from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires, Structures, Variants


# Create your views here.

def home(request, user_name):
	user = User.objects.filter(name = user_name)
	repertoires = Repertoires.objects.filter(user = user_name)
	return render(request, 'home.html', 
	{'user': user, 'repertoires': repertoires})

def new_repertoire(request, user_name):
	user = User.objects.filter(name = user_name)
	return render(request, 'new_repertoire.html', { 'user' : user})

def process_new_repertoire(request):
	if request.method =='POST':
		repertoire_name = request.POST.get('repertoire_name')
		repertoire_color = request.POST.get('repertoire_color')
		user = request.POST.get('user')
		repertoire = Repertoires(repertoire_name=repertoire_name,
		repertoire_color=repertoire_color, user=user)
		repertoire.save()
		return HttpResponse("Nuevo Repertorio Creado")
	else:
		return HttpResponse("Error al crear el repertorio")

def structures(request):
	structures = Structures.objects.all()
	return render(request, 'structures.html', {'structures': structures})

def variants(request, structure_name):
	variants = Variants.objects.filter(structures = structure_name)
	return render(request, 'variants.html', {'variants': variants})
