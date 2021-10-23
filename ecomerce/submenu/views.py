
from django.shortcuts import render, redirect
from django.http.response import HttpResponse


from vestas_usuario.models import Producto 
from django.views.generic import  View ,TemplateView , ListView , UpdateView ,CreateView , DeleteView ,DetailView
from django.urls import reverse_lazy
from django.db.models import Q


class busqueda_por_marcas(View):
	model = Producto
	template_name='submenu_template/arsen2.html'
	

	

	def get(self , request , *args , **kwargs):
		dato = request.GET.get("select")
		print(dato)

		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = dato)|
			Q(description__icontains = dato )

			).distinct()

		print(context)

		

		return render(request , self.template_name , context)








class sub_menu_foton(TemplateView):
	template_name= 'submenu_template/sub_foton.html'


class sub_menu_bicicleta_electrica(TemplateView):
	template_name= 'submenu_template/bicicleta_electrica.html'	



class sub_menu_moto_electrica(TemplateView):
	template_name= 'submenu_template/moto_electrica.html'


class sub_menu_moto_clasica(TemplateView):
	template_name= 'submenu_template/moto_clasicas.html'



class Otras_marcas_moto(TemplateView):
	template_name= 'submenu_template/Otras_marcas_moto.html'


class aceitesubmenu(TemplateView):
	template_name= 'submenu_template/aceitesubmenu.html'

class repuestosubmenu(TemplateView):
	template_name= 'submenu_template/repuestosubmenu.html'					



class moto_clasica_1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Arsen')|
			Q(description__icontains = 'Arsen' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class moto_clasica_2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Horse')|
			Q(description__icontains = 'Horse' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class moto_clasica_3(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Outloock')|
			Q(description__icontains = 'Outloock' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class moto_clasica_4(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'owen')|
			Q(description__icontains = 'owen' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class moto_clasica_5(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'RK6')|
			Q(description__icontains = 'RK6' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class moto_clasica_6(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Silverblade')|
			Q(description__icontains = 'Silverblade' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class moto_clasica_7(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'TX200')|
			Q(description__icontains = 'TX200' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())	



class moto_clasica_8(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Cruiser')|
			Q(description__icontains = 'Cruiser' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class moto_electrica_1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'EK4')|
			Q(description__icontains = 'EK4' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class moto_electrica_2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'GEV1000')|
			Q(description__icontains = 'GEV1000' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class moto_electrica_3(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'HD-1000-ZSN')|
			Q(description__icontains = 'HD-1000-ZSN' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())		





class bicicleta_electrica_1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'City Classica')|
			Q(description__icontains = 'City Classica' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class bicicleta_electrica_2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'EK1')|
			Q(description__icontains = 'EK1' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class bicicleta_electrica_3(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'KALIO')|
			Q(description__icontains = 'KALIO' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class bicicleta_electrica_4(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Maries')|
			Q(description__icontains = 'Maries' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class Triciclo(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Foton')|
			Q(description__icontains = 'Foton' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class Otras_marcas1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'SX-150')|
			Q(description__icontains = 'SX-150' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class Otras_marcas2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'TD-150')|
			Q(description__icontains = 'TD-150' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class aceite_1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Shell 20W50 pote amarillo')|
			Q(description__icontains = 'Shell 20W50 pote amarillo' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class aceite_2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Motoul 3000 20W50')|
			Q(description__icontains = 'Motoul 3000 20W50' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class aceite_3(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Shell 10W40 pote azul')|
			Q(description__icontains = 'Shell 10W40 pote azul' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class aceite_4(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Motoul 5100 15W50')|
			Q(description__icontains = 'Motoul 5100 15W50' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class aceite_5(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Castrol 20W50')|
			Q(description__icontains = 'Castrol 20W50' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())









class repuestos_1(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'aceite')|
			Q(description__icontains = 'aceite' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_2(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Arranque')|
			Q(description__icontains = 'Arranque' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_3(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Asiento')|
			Q(description__icontains = 'Asiento' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_4(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Bateria')|
			Q(description__icontains = 'Bateria' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_5(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'bujia')|
			Q(description__icontains = 'bujia' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())				




class repuestos_6(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Cadena')|
			Q(description__icontains = 'Cadena' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_7(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Carburador')|
			Q(description__icontains = 'Carburador' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_8(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Casco')|
			Q(description__icontains = 'Casco' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_9(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Caucho')|
			Q(description__icontains = 'Caucho' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class repuestos_10(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Conjunto posa pies')|
			Q(description__icontains = 'Conjunto posa pies' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_11(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Coronas')|
			Q(description__icontains = 'Coronas' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_12(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Disco')|
			Q(description__icontains = 'Disco' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_13(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Faro')|
			Q(description__icontains = 'Faro' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_14(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'stop')|
			Q(description__icontains = 'stop' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class repuestos_27(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'filtro')|
			Q(description__icontains = 'filtro' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())

class repuestos_15(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'kit de lubricacion')|
			Q(description__icontains = 'kit de lubricacion' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class repuestos_16(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Luces led')|
			Q(description__icontains = 'Luces led' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class repuestos_17(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Mando de Frenos')|
			Q(description__icontains = 'Mando de Frenos' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_18(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Manzana')|
			Q(description__icontains = 'Manzana' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_19(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'mufle')|
			Q(description__icontains = 'mufle' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_28(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'silenciador')|
			Q(description__icontains = 'silenciador' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())

class repuestos_20(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'odometro')|
			Q(description__icontains = 'odometro' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_21(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'Rin')|
			Q(description__icontains = 'Rin' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())



class repuestos_22(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'tanque')|
			Q(description__icontains = 'tanque' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())


class repuestos_23(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'tapa')|
			Q(description__icontains = 'tapa' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())





class repuestos_24(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'impermiable')|
			Q(description__icontains = 'impermiable' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())









class repuestos_25(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'protectores de mando')|
			Q(description__icontains = 'protectores de mando' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())




class repuestos_26(View):
	model = Producto
	template_name='submenu_template/arsen2.html'

	def get_context_data(self, **kwargs):



		context = {}
		context['dato']= self.model.objects.filter(
			Q(title__icontains = 'candado con alarma')|
			Q(description__icontains = 'candado con alarma' )

			).distinct()

		print(context)

		return context

	def get(self , request , *args , **kwargs):

		return render(request , self.template_name , self.get_context_data())









						


