from django.shortcuts import redirect
from  usuarios.models import Profile, User
from django.contrib.auth import get_user_model
from django.urls import reverse 

class ProfileCompletionMiddleware:

	def __init__(self, get_response):
		

		self.get_response = get_response


	def __call__(self , request):
		User = get_user_model()
		
		if not request.user.is_anonymous:

			query = Profile.objects.filter(user=request.user) 
			if not query:
				profile= Profile(user=request.user)
				
				profile.save() 
			
			


			if  not request.user.is_staff:

				profile= request.user.profile#esto por que es un modelo unido con unser de onetoone
				if not profile.phone_number or not profile.state or not profile.interest:
					if request.path not in [reverse('update_profile') ,reverse('logout') ]:
						return redirect('update_profile')

		response= self.get_response(request)
		return response