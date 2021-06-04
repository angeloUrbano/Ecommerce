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


class ProfileForm(forms.Form):

	email = forms.EmailField(max_length=100 , required=True)
	state = forms.CharField(max_length=500 , required=False)
	phone_number = forms.CharField(max_length=20 , required=False)
	interest = forms.CharField(max_length=20 , required=False)