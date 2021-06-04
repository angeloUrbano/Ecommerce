


class Carro:

	def ___init___(self , request):
		self.request = request
		self.session = request.session
		carro = self.session.get('carro')
		if not carro:
			carro = self.session['carro']={}
		self.carro = carro	


		

	
	def agregar(self , item):

		if str(item.id) not in self.carro.keys(): 
			self.carro[Item.id]={

				'producto_id':item.id,
				'nombre': item.title,
				'precio': item.price,
				'cantidad': 1,
				'imagen': item.image.url

				}	

		else:
			for key , value in self.carro.items():
				if key == str(item.id):
					value["cantidad"]=value["cantidad"]+1
					break


		self.guardar_carro()


	def guardar_carro(self):

		self.session["carro"]= self.carro
		self.session.modified= True
											

	def eliminar(self , item):
		
		item.id = str(item.id)
		if item.id in self.carro:
			del self.carro[item.id]
			self.guardar_carro()


	def restar_producto(self ,item):

		for key , value in self.carro.items():
				if key== str(item.id):
					value["cantidad"]=value["cantidad"]+1
					if value["cantidad"]<1:
						self.eliminar(item)
					break
		self.guardar_carro()



	def limpiar_carro(self):

		self.session["carro"]={}
		self.session.modified= True				
