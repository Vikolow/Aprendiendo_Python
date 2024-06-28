import pickle # Importa el módulo pickle para serialización
from notas import Nota # Importa la clase Nota desde un archivo externo llamado notas.py

class GestorNotas:
	def __init__(self,archivo='notas.pckl'):
		# Inicializa el GestorNotas con un archivo específico para almacenar las notas
		self.archivo=archivo
		try:
			with open(self.archivo,'rb') as f:
				self.notas=pickle.load(f)# Intenta cargar las notas desde el archivo pickle
		except FileNotFoundError:
			self.notas=[] # Si no se encuentra el archivo, inicializa la lista de notas vacía

	# Guarda las notas en el archivo pickle
	def guardar_notas(self):
		with open (self.archivo,'wb') as f:
			pickle.dump(self.notas, f)

	# Agrega una nueva nota al GestorNotas
	def agregar_nota(self,contenido):
		self.notas.append(Nota(contenido))
		self.guardar_notas()
	# Retorna todas las notas almacenadas
	def leer_notas(self):
		return self.notas
	 # Busca notas que coincidan con el texto proporcionado
	def buscar_nota(self,buscar_texto):
		return[nota for nota in self.notas if nota.coincide(buscar_texto) ]
	# Elimina la nota en el índice proporcionado
	def eliminar_nota(self,indice):
		if 0<= indice < len(self.notas):
			del self.notas[indice]
			self.guardar_notas()# Guarda las notas actualizadas después de la eliminación
			print(f"\n[+]Se ha eliminado la nota numero:{indice+1}")
		else:
			print(f"\n[!]No se ha proporcionado un indice correcto\n")


