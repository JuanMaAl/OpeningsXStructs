from django.http import HttpResponse
from django.shortcuts import render
from .models import Structures, Variants


# Create your views here.

def structures(request):
	structures = Structures.objects.all()
	return render(request, 'structures.html', {'structures': structures})

def variants(request, structure_name):
	variants = Variants.objects.filter(structures = structure_name)
	return render(request, 'variants.html', {'variants': variants})
