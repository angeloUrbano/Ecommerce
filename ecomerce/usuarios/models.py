from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
	email = models.EmailField(unique=True)
	telefono_regex= RegexValidator(
		regex=r'\+?1?\d{9,15}$',
		message = 'gormato permitido +999999999'
		)
	Telefono = models.CharField(validators=[telefono_regex], max_length=10 )
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS=[ 'username'  ,'Telefono' , 'first_name' , 'last_name'] 





	def __str__(self):
		return '{}'.format(self.email)
	

STATE_CHOICES = (
    ('Amazonas', 'Amazonas'),
    ('Anzoátegui', 'Anzoátegui'),
	('Apure', 'Apure'),
	('Aragua', 'Aragua'),
	('Barinas', 'Barinas'),
	('Bolívar', 'Bolívar'),
	('Carabobo', 'Carabobo'),
	('Cojedes', 'Cojedes'),
	('Delta Amacuro', 'Delta Amacuro'),
	('Distrito' , 'Distrito'),
	('Falcón', 'Falcón'),
	('Guárico', 'Guárico'),
	('Lara', 'Lara'),
	('Mérida', 'Mérida'),
	('Miranda', 'Miranda'),
	('Monagas', 'Monagas'),
	('Nueva Esparta', 'Nueva Esparta'),
	('Portuguesa' , 'Portuguesa'),
	('Sucre', 'Sucre'),
	('Táchira' , 'Táchira'),
	('Trujillo', 'Trujillo'),
	('Vargas', 'Vargas'),
	('Yaracuy', 'Yaracuy'),
	('Zulia', 'Zulia')
)
class Product_of_Interest(models.Model):
	category_name = models.CharField(max_length= 25 )
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True) 


	def __str__(self):
		return '{}'.format(self.category_name) 



#engo que cambiar el blnck de nombre y apellido a false





class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	telefono_regex= RegexValidator(
		regex=r'\+?1?\d{9,15}$',
		message = 'gormato permitido +999999999'
		)
	phone_number = models.CharField(validators=[telefono_regex], max_length=10 )

	
	primer_nombre = models.CharField(max_length=20 , blank=True)
	apellido = models.CharField(max_length=20 , blank=True)
	state= models.CharField(choices=STATE_CHOICES, max_length=20)
	interest= models.ForeignKey(Product_of_Interest, on_delete=models.CASCADE  , null= True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	 



class request_of_product(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	descripcion = models.TextField(blank= False , null = False)
	create = models.DateTimeField(auto_now_add=True)






#caracteristic about user like	