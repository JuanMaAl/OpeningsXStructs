from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires

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
