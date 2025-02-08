from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RepertoireVariants

def add_to_repertoire(request):
	if request.method == 'POST':
		structure = request.POST.get('structure')
		moves = request.POST.get('moves')
		repertoire_name = request.POST.get('repertoire_name')
		user_id = request.POST.get('user_id')
		repertoire_color = request.POST.get('repertoire_color')
		new_variation = RepertoireVariants(
			structure = structure,
			moves = moves,
			repertoire_name = repertoire_name,
			user_id = user_id
		)
		try:
			new_variation.save()
		except:
			messages.error(request, "No puedes tener dos veces la misma variante en el repertorio")
			return redirect(f'/open-repertoire/{ repertoire_name }/{ repertoire_color}/')
		
		return redirect(f'/open-repertoire/{ repertoire_name }/{ repertoire_color}/')
