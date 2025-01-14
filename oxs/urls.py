from django.urls import path
from . import views

urlpatterns = [
	path('structures/', views.structures, name='structures'),
	path('variants/<str:structure_name>/', views.variants, 
	name='variants'),
	path('home/<str:user_name>/', views.home, name='home'),
	path('new-repertoire/<str:user_name>/', views.new_repertoire, 
	name='new_repertoire'),
	path('process-new-repertoire/<str:user>/', views.process_new_repertoire, 
	name='process_new_repertoire'),
]
