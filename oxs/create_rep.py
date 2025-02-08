from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Repertoires

# Esta vista sirve para renderizar la plantilla que contiene el
# formulario de creación del nuevo repertorio.

def new_repertoire(request):
	return render(request, 'new_repertoire.html')

# Esta vista sirve para tomar los valores del formulario de creación
# de nuevo repertorio mediante el método POST y con ello crear un nuevo
# registro en la tabla Repertoires.

def process_new_repertoire(request):
	if request.method =='POST':
		user = request.user
		repertoire_name = request.POST.get('repertoire_name')
		repertoire_color = request.POST.get('repertoire_color')
		if Repertoires.objects.filter(user=user, repertoire_name=repertoire_name):
		    return render(request, 'new_repertoire.html', 
				{"error":"No puedes tener dos repertorios con el mismo nombre"})	
		else:
			repertoire = Repertoires(repertoire_name=repertoire_name,
			repertoire_color=repertoire_color, user=user)
			repertoire.save()
			return redirect('/home')
	else:
				return render(request, 'new_repertoire.html', 
				{"error":"Error al crear el repertorio"})
