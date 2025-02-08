from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Repertoires, RepertoireVariants

# Esta vista sirve para cargar la plantilla de eliminación de repertorio.
# También filtra el repertorio que hay que eliminar en la tabla de 
# de repertorios y lo pasa como contexto a la plantilla. 

@login_required(login_url='/')
def delete_repertoire(request, repertoire_name):
	user = request.user
	rep_to_delete = Repertoires.objects.filter(user=user, 
	repertoire_name=repertoire_name)
	context = {
		'repertoire_name' : repertoire_name
	}
	return render(request, 'delete_repertoire.html', context)

# Esta vista sirve para eliminar el repertorio al pulsar el botón de 
# eliminar de la plantilla para eliminar repertorios. Toma los datos 
# usando un método POST sobre el formulario oculto de la plantilla. 
# Finalmente a partir de los datos del contexto borra el registro de
# la tabla Repertoires y borra todos los registros asociados de la tabla
# RepertoireVariants. 

@login_required(login_url='/')
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
