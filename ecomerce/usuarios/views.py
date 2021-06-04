from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from usuarios.models import Profile

from  usuarios.forms import ProfileForm , singupForm
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






"""def update_profile(request):
	profile= request.user.profile #esto es por la relacion onetoone a user

	if request.method=='POST':
		form= ProfileForm(request.POST , request.FILES)#request.FILES POR QUE LOS DATOS DE IMAGEN ESTAN ALLI
		if form.is_valid():

			data= form.cleaned_data
			#import pdb;pdb.set_trace()
			profile.website= data['website']
			profile.biography= data['biography']
			profile.phone_number= data['phone_number']
			profile.picture= data['picture']
			profile.save() 
			url = reverse('detail' , kwargs={'username':request.user.username})
			#reverse contruye una url  lo uso ya que redirec no permite kwargs
			return redirect(url)
			#el kwargs es por que la vista detail resive un argumento


	else:
		form= ProfileForm()

	profile= request.user.profile
	return render(request , 'usuariohtml/update_profile.html',{'profile':profile,'user':request.user , 'form': ProfileForm}	)

"""



def login_view(request):
	"""
	import pdb;pdb.set_trace() esta linea es para manejar la informacion del request
	desde el cmd 


	"""

	if request.method== 'POST':
		print("aquiiiiiiiii")
		#import pdb;pdb.set_trace()
		username = request.POST['username']
		password = request.POST['password']
		print("aquiiiiiiiii")
		user = authenticate(request , username = username , password = password)
		if user :
			login(request , user)
			print("aquiiiiiiiii bla bla bla")
			return redirect('home')
		else:
			return render(request , "sesion/login.html" , {'error': 'Invalid username and password'})	
	return render(request , "sesion/login.html")

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')



def signup(request):

	if request.method =='POST':
		form = singupForm(request.POST)
		#import pdb;pdb.set_trace()


		#print(form)
		if form.is_valid():
			print("aqui")
			form.save()
			return redirect('login')
	else:
		form = singupForm()

	return render(request , 'sesion/signup.html' , {'form':form} )