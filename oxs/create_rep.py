from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Repertoires

def new_repertoire(request):
	return render(request, 'new_repertoire.html')

def process_new_repertoire(request):
	if request.method =='POST':
		user = request.user
		repertoire_name = request.POST.get('repertoire_name')
		repertoire_color = request.POST.get('repertoire_color')
		if Repertoires.objects.filter(user=user, repertoire_name=repertoire_name):
			return HttpResponse("Error: No puedes tener dos repertorios con el mismo nombre")
			
		else:
			repertoire = Repertoires(repertoire_name=repertoire_name,
			repertoire_color=repertoire_color, user=user)
			repertoire.save()
			return redirect('/home')
	else:
		return HttpResponse("Error al crear el repertorio")
