import os
# Importar archivo foráneo
from gestor_notas import GestorNotas

gestor = GestorNotas()  # Inicializar instancia de GestorNotas para gestionar las notas
def imprimir_encabezado():
    print("""
           _____           _   _                   _                    _            
          / ____|         | | (_)                 | |                  | |           
         | |  __  ___  ___| |_ _  ___  _ __     __| | ___   _ __   ___ | |_ __ _ ___ 
         | | |_ |/ _ \/ __| __| |/ _ \| '_ \   / _` |/ _ \ | '_ \ / _ \| __/ _` / __|
         | |__| |  __/\__ \ |_| | (_) | | | | | (_| |  __/ | | | | (_) | || (_| \__ \\
         \ _____|\___||___/\__|_|\___/|_| |_|  \__,_|\___| |_| |_|\___/ \__\__,_|___/
                                                                             
    """)
    print("Desarrollado por:Vikolow")


def main():
    while True:
                                                                                                                                    
        imprimir_encabezado()
        print(f"\n---------------\nMenu\n---------------")
        print("1-Agregar una nota")
        print("2-Leer notas")
        print("3-Buscar por una nota")
        print("4-Eliminar una nota")
        print("5-Salir")
        
        try:
            opcion = int(input("\n[+]Introduce una opcion: "))
        except ValueError:
             # Manejo de error si la opción ingresada no es un número
            print("\n [!] La opción indicada es incorrecta. Debe ser un número.\n")
            input(f"\nPresiona <Enter> para continuar...")
            os.system("cls" if os.name == 'nt' else 'clear')  # Limpia la pantalla antes de continuar
            continue
        #Escribir en una nota
        if opcion == 1:
            contenido = input("\n[+]Contenido de la nota: ")
            gestor.agregar_nota(contenido)
        #Leer las notas 
        elif opcion == 2:
            notas = gestor.leer_notas()
            print("\n[+]Mostrando todas las notas almacenadas: \n")
            for i, nota in enumerate(notas):
                print(f"{i+1}:{nota}")
        #Buscar un texto determinado en todas las notas
        elif opcion == 3:
            buscar_texto = input("\n[+]Introduce el texto a buscar en tus notas: ")
            notas = gestor.buscar_nota(buscar_texto)
            print("\n Mostrando las notas que coinciden con el criterio: \n")
            for i, nota in enumerate(notas):
                print(f"\n{i+1}: {nota}")
        #Eliminar una nota determinada
        elif opcion == 4:
            notas = gestor.leer_notas()
            if not notas:
                print("\n[!] No hay notas almacenadas para eliminar.\n")
                continue

            print("\n[+]Mostrando todas las notas almacenadas: \n")
            for i, nota in enumerate(notas):
                print(f"{i+1}. {nota}")

            try:
                indice = int(input("\n[+] Introduce el índice de la nota a eliminar: ")) - 1
            except ValueError:
                print("\n [!] El índice indicado es incorrecto. Debe ser un número.\n")
                continue

            gestor.eliminar_nota(indice)
           
        #Salir del programa
        elif opcion == 5:
            break
        else:
            print("\n [!] La opción indicada es incorrecta\n")

        
        input(f"\nPresiona <Enter> para continuar...")
        os.system("cls" if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
