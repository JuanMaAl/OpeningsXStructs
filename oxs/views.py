from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Repertoires, Structures, Variants


# Create your views here.

def home(request, user_name):
	user = User.objects.filter(name = user_name)
	repertoires = Repertoires.objects.filter(user = user_name)
	return render(request, 'home.html', 
	{'user': user, 'repertoires': repertoires})

def structures(request):
	structures = Structures.objects.all()
	return render(request, 'structures.html', {'structures': structures})

def variants(request, structure_name):
	variants = Variants.objects.filter(structures = structure_name)
	return render(request, 'variants.html', {'variants': variants})
