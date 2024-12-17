from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.hello_juan, name='hello_juan'),
	path('structures/', views.structures, name='structures'),
]
