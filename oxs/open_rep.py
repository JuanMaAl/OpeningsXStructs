from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import RepertoireVariants

# Esta vista sirve para cargar la plantilla de repertorio abierto pasándole
# el contexto que es previamente filtrado en RepertoireVariants. 

@login_required(login_url='/')
def open_repertoire(request, repertoire_name, repertoire_color):
	try:
		user = request.user
		variants = RepertoireVariants.objects.filter(user_id=user, repertoire_name = repertoire_name).order_by('structure')
	except RepertoireVariants.DoesNotExist:
		variants = []
	context = {
		'user' : user,
		'repertoire_name' : repertoire_name,
		'repertoire_color' : repertoire_color,
		'variants' : variants
	}
	return render(request, 'open_repertoire.html', context)
