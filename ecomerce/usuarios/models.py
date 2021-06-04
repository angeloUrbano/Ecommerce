from django.db import models
from django.contrib.auth.models import User
# Create your models here.





STATE_CHOICES = (
    ('CB', 'Carabobo'),
    ('MRY', 'Maracay'),
    ('CSS', 'Caracas')
)
class Product_of_Interest(models.Model):
	category_name = models.CharField(max_length= 25 )
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)


	def __str__(self):
		return '{}'.format(self.category_name) 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number= models.CharField(max_length=20 , blank=True)
	email = models.EmailField(null=False)
	state= models.CharField(choices=STATE_CHOICES, max_length=2)
	interest= models.ForeignKey(Product_of_Interest, on_delete=models.CASCADE  , null= True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	def __str__(self):
		return '{}'.format(self.user.username) 


#caracteristic about user like	