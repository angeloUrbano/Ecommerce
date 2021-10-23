from django import forms
from django.contrib.auth.models import User
from usuarios.models import Profile , Product_of_Interest







class singupForm(forms.Form):
	username = forms.CharField( min_length=4 , max_length=50)
	password= forms.CharField(max_length=70 , widget=forms.PasswordInput())
	password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput())
	first_name= forms.CharField(min_length=2 , max_length=50)
	last_name= forms.CharField(min_length=2 , max_length=50)
	email = forms.CharField(min_length=6 , max_length=70, widget=forms.EmailInput())
	


	def clean_username(self):

		username = self.cleaned_data['username']
		q = User.objects.filter(username=username).exists()
		if q:
		
			raise forms.ValidationError('Username is already in use') 

		return username	

	def clean(self):
		data = super().clean()

		password= data['password']
		password_confirmation = data['password_confirmation']

		if password != password_confirmation:
			raise forms.ValidationError('Passwords do not match')

		return data	

	def save(self):
		#esta funcion es para guardar los datos
		data = self.cleaned_data
		data.pop('password_confirmation')#este campo es para eliminar por que no lo necesito
		user= User.objects.create_user(**data)
		profile= Profile(user=user)
		profile.save()

class ProfileForm(forms.ModelForm):

	class Meta:
		model=Profile

		fields=[ 'primer_nombre' , 'apellido', 'state' , 'phone_number' , 'interest'  ]


		labels = {
			'primer_nombre': 'Nombre',
			'apellido': 'Apellido',
			'state': 'Estado',
			'phone_number': 'Telefono',
			'interest': 'Tipo de moto que posees ',
			}
		widgets = {
			'primer_nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'state' : forms.Select(attrs={'class':'form-control'}),
			'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
			'interest' : forms.Select(attrs={'class':'form-control'})
		}







	