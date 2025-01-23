from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import RepertoireVariants

def del_from_repertoire(request):
	if request.method == 'POST':
		print(request.POST)
		structure = request.POST.get('structure')
		moves = request.POST.get('moves')
		repertoire_name = request.POST.get('repertoire_name')
		user_id = request.POST.get('user_id')
		repertoire_color = request.POST.get('repertoire_color')
		del_variation = RepertoireVariants.objects.get(
			structure = structure,
			moves = moves,
			repertoire_name = repertoire_name,
			user_id = user_id
		)
		del_variation.delete()
		return redirect(f'/open-repertoire/{ user_id }/{ repertoire_name }/{ repertoire_color}/')
