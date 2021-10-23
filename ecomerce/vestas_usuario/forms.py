from django import forms

from vestas_usuario.models import Producto , Order , date_capana


class reporte(forms.Form):
	Vehiculo= forms.CharField( min_length=4 , max_length=50 , required= False)
	
	precio = forms.CharField(min_length=2 , max_length=50 , required= False)
	
	email = forms.CharField(min_length=6 , max_length=70, widget=forms.EmailInput() , required= False)

	fecha = forms.SelectDateWidget()


class ProductForm(forms.ModelForm):

	class Meta:
		model=Producto

		fields=['title' , 'price' ,  'discount_price' , 'description' , 'image' , 'image2' ,
		'image3' ,'image4' ,'detalle' , 'detalle2' , 'detalle3' , 'detalle4'  , 'categoria' , 'disponible']


		labels = {
			'title': 'title',
			'price': 'price',
			'discount_price': 'discount_price',
			'image': 'Cambiar Imagen',
			'image2': 'image2',
			'image3': 'image3',
			'image4': 'image4',
			'detalle' : 'detalle',
			'detalle2': 'detalle',
			'detalle3': 'detalle',
			'detalle4': 'detalle',
			'categoria': 'Categoria',
			'disponible': 'disponible',
			

			}
		widgets = {

			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'price' : forms.NumberInput(attrs={'class':'form-control'}),
			'discount_price' : forms.NumberInput(attrs={'class':'form-control'}),
			
			'detalle' : forms.TextInput(attrs={'class':'form-control'}),
			'detalle2' : forms.TextInput(attrs={'class':'form-control'}),
			'detalle3' : forms.TextInput(attrs={'class':'form-control'}),
			'detalle4' : forms.TextInput(attrs={'class':'form-control'}),
			'categoria' : forms.CheckboxSelectMultiple(),
			'disponible' : forms.CheckboxInput(),
			
			
		}

		



class Pago(forms.Form):

	class Meta:
		model=Order

		fields=['pago_realizado']


		labels = {
			'pago_realizado': 'Pago Realizado',
			
			}
		widgets = {
			'pago_realizado' : forms.CheckboxInput(),
			
			
		}



class campana(forms.ModelForm):

	
	class Meta:
		model=date_capana
 
		fields=['producto'  , 'nombre_campana']


		labels = {
			'producto': 'producto',
			'nombre_campana': 'Descripcion',
			
			}
		widgets = {
			'producto' : forms.CheckboxSelectMultiple(),
			'nombre_campana' : forms.TextInput(attrs={'class':'form-control'}),
			
			
		}





		