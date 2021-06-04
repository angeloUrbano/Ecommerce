from django.shortcuts import render, redirect

from vestas_usuario.models import Producto
from django.views.generic import  View ,TemplateView , ListView , UpdateView ,CreateView , DeleteView
from django.urls import reverse_lazy










class list_article(ListView):

	model:Producto
	template_name = 'usuario/listproduc.html'
	queryset = Producto.objects.all()
	context_object_name ='Producto' 






