from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Repertoires, RepertoireVariants

def delete_repertoire(request, repertoire_name):
	user = request.user
	rep_to_delete = Repertoires.objects.filter(user=user, 
	repertoire_name=repertoire_name)
	context = {
		'repertoire_name' : repertoire_name
	}
	return render(request, 'delete_repertoire.html', context)

def process_delete_repertoire(request, repertoire_name):
	if request.method =='POST':
		user = request.user
		try:
			repertoire = Repertoires.objects.get(user=user, 
			repertoire_name=repertoire_name)
			repertoire.delete()
			RepertoireVariants.objects.filter(user_id=user, 
			repertoire_name=repertoire_name).delete()
			return redirect("/home")
		except Repertoires.DoesNotExist:
			return HttpResponse("Error no se encuentra el repertorio")
	else:
		return HttpResponse("Error al borrar el repertorio")
