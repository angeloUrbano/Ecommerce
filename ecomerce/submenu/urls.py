from django.urls import path 
from .views import(moto_clasica_1,
					moto_clasica_2,
					moto_clasica_3,
					moto_clasica_4,
					moto_clasica_5,
					moto_clasica_6,
					moto_clasica_7,
					moto_clasica_8,





					moto_electrica_1,
					moto_electrica_2,
					moto_electrica_3,




					bicicleta_electrica_1,
					bicicleta_electrica_2,
					bicicleta_electrica_3,
					bicicleta_electrica_4,



					Triciclo,




					Otras_marcas1,
					Otras_marcas2,


					aceite_1,
					aceite_2,
					aceite_3,
					aceite_4,
					aceite_5,


					repuestos_1,
					repuestos_2,
					repuestos_3,
					repuestos_4,
					repuestos_5,
					repuestos_6,
					repuestos_7,
					repuestos_8,
					repuestos_9,
					repuestos_10,
					repuestos_11,
					repuestos_12,
					repuestos_13,
					repuestos_14,
					repuestos_15,
					repuestos_16,
					repuestos_17,
					repuestos_18,
					repuestos_19,
					repuestos_20,
					repuestos_21,
					repuestos_22,
					repuestos_23,
					repuestos_24,
					repuestos_25,
					repuestos_26,
					repuestos_27,
					repuestos_28,

					sub_menu_foton,
					sub_menu_bicicleta_electrica,
					sub_menu_moto_electrica,
					sub_menu_moto_clasica,
					Otras_marcas_moto,
					aceitesubmenu,
					repuestosubmenu,
					busqueda_por_marcas,

				









					

				 ) 

app_name='datos_submenu'


urlpatterns = [ 
	path('moto1/'  , moto_clasica_1.as_view() ,  name='arsen2'),
	path('moto2/'  , moto_clasica_2.as_view() ,  name='moto2'),
	path('moto3/'  , moto_clasica_3.as_view() ,  name='moto3'),
	path('moto4/'  , moto_clasica_4.as_view() ,  name='moto4'),
	path('moto5/'  , moto_clasica_5.as_view() ,  name='moto5'),
	path('moto6/'  , moto_clasica_6.as_view() ,  name='moto6'),
	path('moto7/'  , moto_clasica_7.as_view() ,  name='moto7'),
	path('moto8/'  , moto_clasica_8.as_view() ,  name='moto8'),





	path('moto_electrica1/'  , moto_electrica_1.as_view() ,  name='moto_electrica1'),
	path('moto_electrica2/'  , moto_electrica_2.as_view() ,  name='moto_electrica2'),
	path('moto_electrica3/'  , moto_electrica_3.as_view() ,  name='moto_electrica3'),





	path('bicicleta_electrica1/'  , bicicleta_electrica_1.as_view() ,  name='bicicleta_electrica1'),
	path('bicicleta_electrica2/'  , bicicleta_electrica_2.as_view() ,  name='bicicleta_electrica2'),
	path('bicicleta_electrica3/'  , bicicleta_electrica_3.as_view() ,  name='bicicleta_electrica3'),
	path('bicicleta_electrica4/'  , bicicleta_electrica_4.as_view() ,  name='bicicleta_electrica4'),




	path('Triciclo1/'  , Triciclo.as_view() ,  name='Triciclo1'),






	path('Otras_1/'  , Otras_marcas1.as_view() ,  name='Otras_1'),
	path('Otras_2/'  , Otras_marcas2.as_view() ,  name='Otras_2'),


	path('aceite1/'  , aceite_1.as_view() ,  name='aceite1'),
	path('aceite2/'  , aceite_2.as_view() ,  name='aceite2'),
	path('aceite3/'  , aceite_3.as_view() ,  name='aceite3'),
	path('aceite4/'  , aceite_4.as_view() ,  name='aceite4'),
	path('aceite5/'  , aceite_5.as_view() ,  name='aceite5'),




	path('repuesto1/'  , repuestos_1.as_view() ,   name='repuesto1'),
	path('repuesto2/'  , repuestos_2.as_view() ,   name='repuesto2'),
	path('repuesto3/'  , repuestos_3.as_view() ,   name='repuesto3'),
	path('repuesto4/'  , repuestos_4.as_view() ,   name='repuesto4'),
	path('repuesto5/'  , repuestos_5.as_view() ,   name='repuesto5'),
	path('repuesto6/'  , repuestos_6.as_view() ,   name='repuesto6'),
	path('repuesto7/'  , repuestos_7.as_view() ,   name='repuesto7'),
	path('repuesto8/'  , repuestos_8.as_view() ,   name='repuesto8'),
	path('repuesto9/'  , repuestos_9.as_view() ,   name='repuesto9'),
	path('repuesto10/'  , repuestos_10.as_view() , name='repuesto10'),
	path('repuesto11/'  , repuestos_11.as_view() , name='repuesto11'),
	path('repuesto12/'  , repuestos_12.as_view() , name='repuesto12'),
	path('repuesto13/'  , repuestos_13.as_view() , name='repuesto13'),
	path('repuesto14/'  , repuestos_14.as_view() , name='repuesto14'),
	path('repuesto15/'  , repuestos_15.as_view() , name='repuesto15'),
	path('repuesto16/'  , repuestos_16.as_view() , name='repuesto16'),
	path('repuesto17/'  , repuestos_17.as_view() , name='repuesto17'),
	path('repuesto18/'  , repuestos_18.as_view() , name='repuesto18'),
	path('repuesto19/'  , repuestos_19.as_view() , name='repuesto19'),
	path('repuesto20/'  , repuestos_20.as_view() , name='repuesto20'),
	path('repuesto21/'  , repuestos_21.as_view() , name='repuesto21'),
	path('repuesto22/'  , repuestos_22.as_view() , name='repuesto22'),
	path('repuesto23/'  , repuestos_23.as_view() , name='repuesto23'),
	path('repuesto24/'  , repuestos_24.as_view() , name='repuesto24'),
	path('repuesto25/'  , repuestos_25.as_view() , name='repuesto25'),
	path('repuesto26/'  , repuestos_26.as_view() , name='repuesto26'),
	path('repuesto27/'  , repuestos_27.as_view() , name='repuesto27'),
	path('repuesto28/'  , repuestos_28.as_view() , name='repuesto28'),







	path('sub_foton/'  , sub_menu_foton.as_view() , name='sub_fotonn'),
	path('bicicleta_electricasub/'  , sub_menu_bicicleta_electrica.as_view() , name='bicicleta_electricasub'),
	path('moto_electricasub/'  , sub_menu_moto_electrica.as_view() , name='moto_electricasub'),
	path('moto_clasicasub/'  , sub_menu_moto_clasica.as_view() , name='moto_clasicasub'),
	path('Otras_marcas_motosub/'  , Otras_marcas_moto.as_view() , name='Otras_marcas_motosub'),
	path('aceitesub/'  , aceitesubmenu.as_view() , name='aceitesub'),
	path('repuestosub/'  , repuestosubmenu.as_view() , name='repuestosub'),





	path('busqueda_por_marcas1/'  , busqueda_por_marcas.as_view() , name='busqueda_por_marcas1'),



	


	
]