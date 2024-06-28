# Gestor de Notas  

Este proyecto implementa un gestor de notas simple utilizando Python, donde se utiliza la serialización con el módulo `pickle` para almacenar y recuperar datos de manera persistente. La aplicación permite agregar, leer, buscar y eliminar notas utilizando archivos serializados. 

## Funcionalidades 
- **Agregar una nota:** Permite ingresar contenido para crear una nueva nota. 
- **Leer notas:** Muestra todas las notas almacenadas.
- **Buscar por una nota:** Busca notas que contengan un texto específico. 
- **Eliminar una nota:** Permite eliminar una nota seleccionando su índice. 

## Archivos del proyecto  
- **programa_notas.py:** Contiene el programa principal que interactúa con el usuario y gestiona las notas.
- **gestor_notas.py:** Define la clase `GestorNotas`, que proporciona métodos para gestionar las notas utilizando serialización con `pickle`.
- **notas.py:** Contiene la definición de la clase `Nota`, que representa cada nota individual y sus métodos asociados. 

- ## Uso seguro de la serialización
-Es importante considerar los riesgos de seguridad al trabajar con serialización:
- **Validación de datos:** Asegúrate de validar  los datos antes de deserializarlos para prevenir la ejecución de código malicioso. 
- **Integridad de datos:** Verifica la procedencia de los archivos serializados para evitar la manipulación de datos por terceros. En el futuro, planeo explorar más sobre las vulnerabilidades y consecuencias asociadas con la serialización.

- ## Ejecución del programa 
- Para ejecutar el programa, asegúrate de tener Python instalado y sigue estos pasos:  
1. Clona este repositorio en tu máquina local.
2. Abre una terminal o línea de comandos y navega al directorio donde has clonado el repositorio. 
3. Ejecuta el programa principal con el siguiente comando:   python programa_notas.py``

## Contribuciones

Si encuentras errores o deseas mejorar el proyecto, ¡siéntete libre de hacer un fork del repositorio y enviar un pull request!Cualquier mejora sera bien recibida y agradecida!



