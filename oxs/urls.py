from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.login_user, name='login_user'),

	path('structures/<str:user>/<str:repertoire_name>/<str:repertoire_color>/', views.structures, name='structures'),
	
	path('variants/<str:user>/<str:repertoire_name>/<str:repertoire_color>/<str:structure_name>/', views.variants, 
	name='variants'),
	
	path('home/<str:user_name>/', views.home, name='home'),
	
	path('new-repertoire/<str:user_name>/', views.new_repertoire, 
	name='new_repertoire'),
	
	path('process-new-repertoire/<str:user>/', 
	views.process_new_repertoire, 
	name='process_new_repertoire'),

	path('open-repertoire/<str:user>/<str:repertoire_name>/<str:repertoire_color>/',
	views.open_repertoire, name='open_repertoire'),

	path('add-to-repertoire/',
	views.add_to_repertoire, name='add_to_repertoire'),

	path('del-from-repertoire/',
	views.del_from_repertoire, name='del_from_repertoire'),

	path('delete-repertoire/<str:user>/<str:repertoire_name>/',
	views.delete_repertoire, name='delete_repertoire'),

	path('process-delete-repertoire/<str:user>/<str:repertoire_name>/',
	views.process_delete_repertoire, name='process_delete_repertoire'),
]
