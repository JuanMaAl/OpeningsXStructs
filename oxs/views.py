from django.http import HttpResponse
from django.shortcuts import render
from .models import Structures


# Create your views here.

#def structures(request):
#	structures = Structures.object.all()
#	return render(request, 'structures.html', {'structures': structures})

def hello_juan(request):
	return HttpResponse("Hello, Juan!")
