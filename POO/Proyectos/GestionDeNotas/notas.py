
class Nota:

	def __init__(self,contenido):
		 # Inicializa una nueva nota con el contenido proporcionado
		self.contenido=contenido
	def coincide(self,buscar_texto):
		# Verifica si el texto de búsqueda coincide con el contenido de la nota
		return buscar_texto in self.contenido
	# Retorna una representación en cadena de la nota (su contenido)
	def __str__(self):
		return self.contenido