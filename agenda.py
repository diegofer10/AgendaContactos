# Agenda que almacena datos de contacto

import os   # Librerias y archivos

CARPETA = 'contactos/'  # Carpeta de contactos
EXTENSION = '.txt'


class Contacto: 

    def __init__(self, nombre,telefono, categoria):
        self.nombre= nombre
        self.telefono = telefono
        self.categoria= categoria





def app():
    #Revisa si existe la carpeta
    crear_directorio()

    #Muestra Menu de Opciones
    mostrar_menu()

    #Preguntar Opciones
    preguntar =True
    while preguntar: 
        opcion = input('Seleccione una opcion: \n')
        opcion = int(opcion)
        #Ejecuta las opciones
        if opcion == 1: 
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            listar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 0:
            break
        else: 
            raise Exception("Opcion no valida")




#_____________________________________________________    
#FUNCIONES 
#_____________________________________________________    
def eliminar_contacto():
    print('Escribe el nombre del contacto a eliminar:')
    nombre_eliminar= input('Nombre: \r\n')

    try:
        os.remove(CARPETA+ nombre_eliminar+ EXTENSION)
        print('Eliminado corectamente')
    except IOError:
         print('________________________________________')
         print('****Error en la eliminacion del contacto ***')
         print('________________________________________')

    #Reiniciar la APP
    app()
#_____________________________________________________    
def buscar_contacto():
    print('Escribe el nombre del contacto a buscar:')
    nombre_buscar= input('Nombre: \r\n')


    try:
        with open (CARPETA + nombre_buscar + EXTENSION) as contacto:
            print('__________________________________')
            print('\r\n Informacion de Contacto \r\n ')
            for linea in contacto:
                print(linea.rstrip())
            print('__________________________________')
    except IOError:
         print('________________________________________')
         print('****Error en la busqueda de contacto ***')
         print('________________________________________')

    #Reiniciar la APP
    app()

#_____________________________________________________
def listar_contacto():
    
    archivos=os.listdir(CARPETA)

    #Valido que solo muestre los txt
    archivo_txt = [ i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivo_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto: 
                print(linea.rstrip()) ##recorro el archivo txt
        print ('--------------------------\r\n')
    #Reiniciar la APP
    app()
#_____________________________________________________
def agregar_contacto():
    print('Escribe los datos para agregar el contacto:')
    nombre= input('Nombre: \r\n')

    #Validar que el archivo ya  existe
    existe = exisiste_contacto(nombre)

    if not existe:
        
    #Escribo el archivo
        with open (CARPETA + nombre + EXTENSION, 'w') as archivo:
            
            telefono= input('Telefono: \r\n')
           
            categoria= input('Categoria: \r\n')
            
            #Instanciar la Clase
            contacto= Contacto(nombre, telefono,categoria)

            #Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n') 
            archivo.write('Telefono:' + contacto.telefono + '\r\n') 
            archivo.write('Categoria:' + contacto.categoria + '\r\n') 

            #carga Ok
            print("\n\r Contacto cargador correctamente \n\r")
    else: 
        print('El Contacto ya existe')
    
    #Reiniciar la APP
    app()
    




#_____________________________________________________
def editar_contacto():
    print('Escribe el nombre del contacto a editar \r\n')
    nombre_anterior= input('Nombre a editar: \r\n')
 
 
    #Validar que el archivo ya  existe
    existe = exisiste_contacto( nombre_anterior)
    
    if existe:
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre= input('Agrega nuevo nombre: \r\n')
            telefono= input('Agrega nuevo Telefono: \r\n')
            categoria= input('Agrega nueva Categoria: \r\n')

          #Intancio
            contacto = Contacto(nombre,telefono,categoria)

          #Escribo en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n') 
            archivo.write('Telefono:' + contacto.telefono + '\r\n') 
            archivo.write('Categoria:' + contacto.categoria + '\r\n') 
        
           #Renombro el archivos
        os.rename(CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre + EXTENSION )
          #carga Ok
        print("\n\r Contacto EDITADO correctamente \n\r")

    else: 
        print('No puedes editar el contacto')


    #Reiniciar la APP
    app()


#_____________________________________________________
def exisiste_contacto(nombre:str):
    """AI is creating summary for exisiste_contacto

    Args:
        nombre ([type]): [nombre de contacto a editar]
    
    Return:
        nombre del contacto editar
    """
    return os.path.isfile(CARPETA + nombre + EXTENSION)

  



    


#_____________________________________________________
def mostrar_menu():
    print("_________________________")
    print("Seleccciones la opcion: ")
    print("(1) Agregar Contacto")
    print("(2) Editar Contacto")
    print("(3) Listar Contacto")
    print("(4) Buscar Contacto")
    print("(5) Eliminar Contacto")
    print("(0) Salir")
    print("_________________________")
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
     
#_____________________________________________________
#Llamo a la App
app()