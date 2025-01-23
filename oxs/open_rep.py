from django.http import HttpResponse
from django.shortcuts import render
from .models import RepertoireVariants

def open_repertoire(request, user, repertoire_name, repertoire_color):
	try:
		variants = RepertoireVariants.objects.filter(user_id=user, repertoire_name = repertoire_name)
	except RepertoireVariants.DoesNotExist:
		variants = []
	context = {
		'user' : user,
		'repertoire_name' : repertoire_name,
		'repertoire_color' : repertoire_color,
		'variants' : variants
	}
	return render(request, 'open_repertoire.html', {'context':context})
