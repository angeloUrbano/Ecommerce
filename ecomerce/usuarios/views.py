from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView , DetailView , View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from usuarios.models import Profile , User
from django.contrib.auth import get_user_model

from  usuarios.forms import  ProfileForm , singupForm
from django.core.mail import EmailMessage
from django.contrib import messages

from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
from .utils import token_generator

from django.utils.encoding import force_bytes , force_text , DjangoUnicodeDecodeError

from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site

# Create your views here.




"""class UserDetail(DetailView):


	template_name='usuariohtml/detail.html'
	slug_field= 'username'#esto es como si fuera el pk por que el username es unico en mi programa
	slug_url_kwarg= 'username'# el valor que entra en la url
	queryset= User.objects.all()

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		user = self.get_object()
		
		segun la documentacion esta funcion self.get_object() de encarga de hacer
		el query segun el objeto que nosotros le pasamos 
		
		context['posts']= Post.objects.filter(user=user).order_by('-created')
		return context"""






def update_profile(request):
	User = get_user_model()
	profile= request.user.profile #esto es por la relacion onetoone a user

	print(request.POST)
	if request.method=='POST':
		form= ProfileForm(request.POST)#request.FILES POR QUE LOS DATOS DE IMAGEN ESTAN ALLI
		if form.is_valid():
			print('en formulario valido')
			data= form.cleaned_data
			#import pdb;pdb.set_trace()
			profile.interest= data['interest']
			profile.state= data['state']
			profile.phone_number= data['phone_number']
			profile.primer_nombre= data['primer_nombre']
			profile.apellido= data['apellido']
			
			profile.save() 
			#url = reverse('detail' , kwargs={'username':request.user.username})
			#reverse contruye una url  lo uso ya que redirec no permite kwargs
			print('aqui estoy3')
			return redirect('ventas:articulos')
			#el kwargs es por que la vista detail resive un argumento


	else:
		
		form= ProfileForm()
	
	profile= request.user.profile
	return render(request , 'usuario/update_profile.html',{'profile':profile,'user':request.user , 'form': form}	)





def login_view(request):
	"""
	import pdb;pdb.set_trace() esta linea es para manejar la informacion del request
	desde el cmd 


	"""

	if request.method== 'POST':
		print("aquiiiiiiiii")
		#import pdb;pdb.set_trace()
		email = request.POST['email']
		password = request.POST['password']
		
		User = authenticate(request , email = email, password = password)
		print(email)
		print(password)
		if User :
			login(request , User)
			
			return redirect('home')
		else:
			return render(request , "sesion/login.html" , {'error': 'Correo o Contraseña Invalido'})	
	return render(request , "sesion/login.html")

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')

	



class signup (View):
	def get(self, request):
		return render(request, 'sesion/signup.html')

	def post(self, request):
        

		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']
		context = {
			'fieldValues': request.POST
 		}
		

		if password != password_confirmation:
			
			return render(request , "sesion/signup.html" , {'error': 'las Contraseñas No coinciden'})
		User = get_user_model()
		if  User.objects.filter(email=email).exists():
			return render(request , "sesion/signup.html" , {'error': 'Correo en uso'})

		if not User.objects.filter(email=email).exists():
			#return render(request , "sesion/signup.html" , {'error': 'Correo en uso'})
			
			
				
			if len(password) < 6:
				return render(request , "sesion/signup.html" , {'error': 'la Contraseña debe tener mas de 6 caracteres'})
				return render(request , "sesion/signup.html" , context)
	
			User = User.objects.create_user(username=username, email=email)
			User.set_password(password)
			User.is_active = False
			User.save()
			
			

			profile= Profile(user=User)
			
			profile.save()
			
			print('aqui en el registro')
			current_site = get_current_site(request)
			email_body = {
				'user': User,
 				'domain': current_site.domain,
 				'uid': urlsafe_base64_encode(force_bytes(User.pk)),
 				'token': token_generator.make_token(User),
 			}

			link = reverse('token:activate', kwargs={
				'uidb64': email_body['uid'], 'token': email_body['token']})

			email_subject = 'Activate your account'

			activate_url = 'http://'+current_site.domain+link
			#data= form.cleaned_data 


			subjects= 'activa tu cuenta'
			message= 'verifica tu cuenta\n'+activate_url 
			email_from=settings.EMAIL_HOST_USER
			
			RECIPIENT_LIST=[email]

			send_mail(subjects , message , email_from , RECIPIENT_LIST)
			return render(request, 'sesion/signup.html', {'error': 'Revisar Correo electronico'})		
		print('redirijo')	
		return render(request, 'sesion/signup.html')
			
			
	

	




class verification (View):

	def get(self, request, uidb64, token):
		try:
			id = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=id)

			if not token_generator.check_token(user, token):
				return redirect('login'+'?message='+'User already activated')

			if user.is_active:
				return redirect('login')
			user.is_active = True
			user.save()

			messages.success(request, 'Account activated successfully')
			return redirect('login')

		except Exception as ex:
			pass

		return redirect('login')
