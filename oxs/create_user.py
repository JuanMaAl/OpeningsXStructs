from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError 

def new_user(request):
	return render(request, 'new_user.html')

def process_new_user(request):
	if request.method =='POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 == password2:
			try:
				user = User.objects.create_user(username, email, password1)
				login(request, user)
				return redirect('/home')
			except IntegrityError:
				return render(request, 'new_user.html', 
				{"error":"El nombre de usuario ya existe"})
		else:
				return render(request, 'new_user.html', 
				{"error":"Las contraseñas no coinciden"})

