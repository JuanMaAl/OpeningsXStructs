from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Esta vista sirve para iniciar la sesión del usuario. Obtiene los datos
# que el usuario ha introducido en el formulario de login y las compara
# con los guardados en la base de datos usando función authenticate.
# si todo esta bien inicia sesión y redirige al home del usuario. 

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect (f'/home')
		else:
		        return render(request, 'login.html', 
				{"error":"Login fallido, usuario o password incorrecto"})

	return render(request, 'login.html')

# Esta vista sirve para cerrar la sesión del usuario. 

def logout_user(request):
	logout(request)
	return redirect('/')
