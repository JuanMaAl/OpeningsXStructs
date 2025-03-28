from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import RepertoireVariants

# Esta vista sirve para eliminar una variante. Toma los datos de un 
# formulario oculto asociado al botón Eliminar asociado a la variante
# concreta. Con los datos obtenidos del método post borra el registro de
# la tabla RepertoireVariants

def del_from_repertoire(request):
	if request.method == 'POST':
		structure = request.POST.get('structure')
		moves = request.POST.get('moves')
		repertoire_name = request.POST.get('repertoire_name')
		repertoire_color = request.POST.get('repertoire_color')
		user_id = request.user
		del_variation = RepertoireVariants.objects.get(
			structure = structure,
			moves = moves,
			repertoire_name = repertoire_name,
			user_id = user_id
		)
		del_variation.delete()
		return redirect(f'/open-repertoire/{ repertoire_name }/{ repertoire_color}/')
