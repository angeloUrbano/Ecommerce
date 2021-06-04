
from django.urls import path 
from .views import (list_article,
					

	)


urlpatterns = [


	path('articulo/' , list_article.as_view() , name='articulos'),
	


]