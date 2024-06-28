from funciones import ver_pintura , agregar_pinturas, exportar_pinturas, eliminar_pintura , buscar_pintura
opc = ['ver listado de pinturas',
       'Buscar pintura',
       'agregar pintura',
       'Eliminar pintura',
       'Exportar pintura']


while True:
    for x , y in enumerate(opc):
        print(f"{x + 1}.{y}")
    ans = input("¿Que desea hacer?\n")    
    if ans == "1":
        ver_pintura()
    elif ans == "2":
        buscar_pintura()   
    elif ans == "3":
        agregar_pinturas()    
    elif ans == "4":
        eliminar_pintura()    
    elif ans == "5":
        exportar_pinturas()    

        
