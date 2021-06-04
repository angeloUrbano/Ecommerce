from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from vestas_usuario.models import Producto  , OrderItem ,  Order
from django.views.generic import  View ,TemplateView , ListView , UpdateView ,CreateView , DeleteView
from django.urls import reverse_lazy
from django.contrib import messages




from  .carro import Carro
# Create your views here.

"""def  agregar_producto(request , producto_id):
	print("aqui")
	print(request)
	print("aqui")

	carro = Carro(request)
	producto = Producto.objects.get(id=producto_id)
	Carro.agregar(producto=producto)
	return redirect('articulos')
	



def  eliminar_producto(request , productoid):
	carro = Carro(request)

	product = Producto.objects.get(id =  producto_id)
	carro.eliminar(Producto= product)

	return redirect('articulos')



def  restar_producto(request , item_id):
	carro = Carro(request)

	product = Producto.objects.get(id =  productoid)
	carro.restar_producto(Producto= product)

	return redirect('articulos')


def  limpiar_carro(request , producto_id):
	carro = Carro(request)

	carro.limpiar_carro()

	return redirect('articulos')	"""





def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order_producto, created = OrderItem.objects.get_or_create(
        producto=producto,
        user=request.user,
        ordered=False 
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.roducto.filter(producto__id=producto.id).exists():
            order_producto.quantity += 1
            order_producto.save()
            messages.info(request, "This item quantity was updated.")
            return redirect('carro:order-summary')
        else:
            order.roducto.add(order_producto)
            messages.info(request, "This item was added to your cart.")
            return redirect('carro:order-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.roducto.add(order_producto)
        messages.info(request, "This item was added to your cart.")
        return redirect('carro:order-summary')


@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.roducto.filter(producto__id=producto.id).exists():
            order_item = OrderItem.objects.filter(
                producto=producto,
                user=request.user,
                ordered=False
            )[0]
            order.roducto.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("carro:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("carro:product", id=producto_id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("carro:product", id=producto_id)


@login_required
def restar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.roducto.filter(producto__id=producto.id).exists():
            order_item = OrderItem.objects.filter(
                producto=producto,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.roducto.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("carro:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("carro:product", id=producto_id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("carro:product", id=producto_id)	


# this view nedd an LoginRequiredMixin
class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'carro/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")        
