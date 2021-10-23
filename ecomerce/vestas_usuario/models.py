from django.db import models
from usuarios.models import Profile , User
from django.conf import settings
#from django.contrib.auth.models import User

# Create your models here.



class Categoria(models.Model):
    
    nombre_categoria= models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre_categoria)


class Producto(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    #category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    image = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    detalle = models.CharField(max_length=100 , blank=True, null=True)
    detalle2 = models.CharField(max_length=100 , blank=True, null=True)
    detalle3 = models.CharField(max_length=100 , blank=True, null=True)
    detalle4 = models.CharField(max_length=100 , blank=True, null=True)
    disponible = models.BooleanField(default=True)
    categoria = models.ManyToManyField(Categoria)    




    def __str__(self):

    	return '{}'.format(self.title)





    



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.producto.title}"

    def get_total_item_price(self):
        return self.quantity * self.producto.price

    def get_total_discount_item_price(self):
        return self.quantity * self.producto.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.producto.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price() 


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    roducto = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False) 
    pago_realizado = models.BooleanField(default=False) 

    def __str__(self):
        return self.user.username




    def get_total(self):
        total = 0
        for order_item in self.roducto.all():
            total += order_item.get_final_price()
        
        return total



class date_capana(models.Model):

  
    nombre_campana  = models.CharField(max_length= 150)
    producto = models.ManyToManyField(Producto)
    creado = models.DateTimeField(auto_now_add=True)
   
    

    
