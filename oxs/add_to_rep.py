from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import RepertoireVariants

def add_to_repertoire(request):
	if request.method == 'POST':
		structure = request.POST.get('structure')
		moves = request.POST.get('moves')
		repertoire_name = request.POST.get('repertoire_name')
		user_id = request.POST.get('user_id')
		user_name = user_id

		new_variation = RepertoireVariants(
			structure = structure,
			moves = moves,
			repertoire_name = repertoire_name,
			user_id = user_id
		)
		new_variation.save()
		return request(f'/home/{ user_name }/')
