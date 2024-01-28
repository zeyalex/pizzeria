"""Визначити URL шаблони для pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
	# Головна сторінка
	path('', views.index, name='index'),
    # Сторінка що відображає всі теми
    path('pizzas/', views.pizzas, name='pizzas'),
    # Сторінка, присвячена окремій темі.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
