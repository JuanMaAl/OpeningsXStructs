from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires, Structures, Variants


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

# Repertoire CRUD Operations 

# START Creating New Repertoire Operation
def new_repertoire(request, user_name):
	user = User.objects.filter(name = user_name)
	return render(request, 'new_repertoire.html', { 'user' : user_name})

def process_new_repertoire(request, user):
	if request.method =='POST':
		repertoire_name = request.POST.get('repertoire_name')
		repertoire_color = request.POST.get('repertoire_color')
		try:
			user = User.objects.get(name = user)
		except User.DoesNotExist:
			return HttpResponse("Error uno al crear el repertorio")
		if Repertoires.objects.filter(user=user, repertoire_name=repertoire_name):
			return HttpResponse("Error: No puedes tener dos repertorios con el mismo nombre")
			
		else:
			repertoire = Repertoires(repertoire_name=repertoire_name,
			repertoire_color=repertoire_color, user=user)
			repertoire.save()
			return HttpResponse("Nuevo Repertorio Creado")
	else:
		return HttpResponse("Error al crear el repertorio")
# END Creating New Repertoire Operation

# START Delete Repertoire Operation

def delete_repertoire(request, user, repertoire_name):
	rep_to_delete = Repertoires.objects.filter(user=user, 
	repertoire_name=repertoire_name)
	context = {
		'user' : user,
		'repertoire_name' : repertoire_name
	}
	return render(request, 'delete_repertoire.html', context)

def process_delete_repertoire(request, user, repertoire_name):
	if request.method =='POST':
		try:
			repertoire = Repertoires.objects.get(user=user, 
			repertoire_name=repertoire_name)
			repertoire.delete()
			return HttpResponse("Repertorio Borrado")
		except Repertoires.DoesNotExist:
			return HttpResponse("Error no se encuentra el repertorio")
	else:
		return HttpResponse("Error al borrar el repertorio")

# END Delete Repertoire Operation
