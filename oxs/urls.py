from django.urls import path
from . import views

urlpatterns = [
	path('structures/', views.structures, name='structures'),
	path('variants/<str:structure_name>/', views.variants, 
	name='variants'),
	path('home/<str:user_name>/', views.home, name='home'),
]
