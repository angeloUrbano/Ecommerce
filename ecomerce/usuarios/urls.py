from django.urls import path 
from .views import (verification ,
					

	)


app_name='token'


urlpatterns = [


	path('activate/<uidb64>/<token>' , verification.as_view() , name='activate'),
	


]