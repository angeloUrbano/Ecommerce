from django.contrib import admin
from vestas_usuario.models import Producto , Categoria ,Profile , Order

# Register your models here.


admin.site.register(Producto)
admin.site.register(Profile)
admin.site.register(Order)

admin.site.register(Categoria)
