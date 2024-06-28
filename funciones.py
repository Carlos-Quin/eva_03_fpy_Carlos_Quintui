
import json
import os

pinturas = []


def limpiar_pantalla():
    os.system("cls")

def agregar_pinturas():
    code = [380560]
    tot = int(code.max(code)+1)
    name = input("Ingrese nombre del color\n")
    tipo = input("Ingrese tipo de pintura(ACRILICO/LATEX)\n")
    value = int(input("Ingrese valor de la pintura\n"))
    stock = input("ingrese el stock\n")
    pintura = [{"Codigo":tot,"Nombre":name,"Tipo":tipo,"Valor":value,"stock":stock}]
    pinturas.append(pintura)
    print("Pintura agregado con exito")
    


def ver_pintura():
    if pinturas == []:
        print("No hay pinturas en la base de datos!")
    else:
        for A in pinturas:
            print(A [pinturas])   

def buscar_pintura():
    Buscando = input("Ingrese nombre o codigo de la pintura")
    if Buscando != [pinturas]:
        print("No existe ninguna pintura")
    else: 
        for la in pinturas:
            print(la[pinturas])


#se me olvido esta wea tengo recuerdos JAJAJ
def eliminar_pintura():
    borrar_libro = input("Ingrese el nombre o el codigo del producto que desea borrar\n") 
    if not borrar_libro:
        print("No existe esta pintura")
    else:
        for llave in pinturas:
            borrar_libro.lower() == llave["pinturas"].lower()

            print("Borrado exitosamente")
            


def exportar_pinturas():
    try:
        with open("archivo.json","w") as archivo:
            json.dumps(pinturas , archivo)
            print('Archivo exportado exitosamente!!')
    except: SyntaxError
    print("La base de datos ya existe")   