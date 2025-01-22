from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires

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
