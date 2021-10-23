
from django.urls import path 
from .views import (list_article,
					Create_Product,
					prequest_of_product,
					update_product,
					delete_product,
					list_request_of_product,
					detail_product,
					contacto,
					seng_message_whatspp,
					Ordenrealizada,
					OrdenrealizadaAdministrativo,
					detalle_compra,
					seng_message_whatspp_2,
					update_Pago,
					reporte_excel,
					send_email,
					index_email,
					try_send_mail,
					create_marketin,
					list_catalogo,
					modal_reporte,
					politica_seguridad,
					ListCatalogo,
					factura,
					detalle_compra_solicitud,
					 

	)

app_name='ventas'
urlpatterns = [ 


	path('' , list_article.as_view() , name='articulos'),
	path('contacto/' , contacto.as_view() , name='contactame'),
	path('create_articulo/' , Create_Product.as_view() , name='create_articulo'),
	path('prest_of_product/' , prequest_of_product , name='prest_of_product_otro'),
	path('editar_producto/<int:pk>' , update_product.as_view() , name='editar_producto'),
	path('eliminar_producto/<int:pk>' , delete_product.as_view() , name='eliminar_producto'),
	path('solicitud/' , list_request_of_product.as_view() , name='solicitud'),
	path('detal/<int:pk>' , detail_product.as_view() , name='detail'),
	path('envio_whatsapp/' , seng_message_whatspp , name='envio_whatsapp'),
	path('orden_realizada/' , Ordenrealizada.as_view() , name='orden_realizada'),
	path('orden_administrador/' , OrdenrealizadaAdministrativo.as_view() , name='orden_administrador'),
	path('envio_whatsapp2/<int:id_dato>' , seng_message_whatspp_2 , name='envio_whatsapp2'),
	path('detalle_compra/<int:pk>' , detalle_compra.as_view() , name='detalle_compra'),
	path('pago_aprobar/<int:pk>' , update_Pago.as_view() , name='pago_aproba'),
	path('Reporte/' , reporte_excel.as_view() , name='Reportar_excel'),
	path('enviar_correo/' , send_email , name='enviar_correo'),
	path('try_correo/' ,try_send_mail , name='try_correo'),
	path('index/' , index_email.as_view() , name='index'),
	path('Marketin/' , create_marketin.as_view() , name='create_Marketin'),
	path('catalogo/' , list_catalogo.as_view() , name='catalogo'),
	path('ListCatalogo/' ,ListCatalogo, name='ListCatalogoo'),
	path('factura/' , factura.as_view() , name='factura'),
	path('reporte/' , modal_reporte.as_view() , name='reporte'),
	path('politicaDeSeguridad/' , politica_seguridad.as_view() , name='politicaDeSeguridad'),
	path('detalle_compra_solicitud1/<int:pk>' , detalle_compra_solicitud.as_view() , name='detalle_compra_solicitud1'),
]