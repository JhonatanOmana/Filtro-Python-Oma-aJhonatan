import json

def abrirArchivo():
    with open ("datos.json","r") as file:
        return json.load(file)

def guardarArchivo():
    with open ("datos.json","w") as file:
        return json.dump(file)  
     


print("---------------------------------------")  
print("|         B I E N V E N I D O         |") 
print("|                 A                   |")
print("|           M O V I S T A R           |")
print("---------------------------------------")    
print("Opciones disponibles :\n1.Iniciar sesion.\n2.Salir")
j=int(input("elije una opcion :"))

if (j==1):
    print("---------------------------------------") 
    print("Deseas ingresar como : \n1.Usuario.\n2.Administrador.")
    h=int(input("Elije un perfil : "))

    if (h==1):
        print("---------------------------------------") 
        print("          ¡BIENVENIDO USUARIO!         ")   
        print("---------------------------------------")  
        print("opciones disponibles : \n1.Servicios utilizados.\n2.Servicio al cliente.\n3.Reclamos.\n4.Sugerencia\n5.Salir")
        k=int(input("Elije una opcion :"))

        if (k==1):
            print("Servicios utliados: ")

        elif (k==2):
            print("---------------------------------------") 
            print("          SERVICIO AL CLIENTE          ")   
            print("---------------------------------------") 
            print(("En que ncesitas ayuda?"))
            help=str(input("Dejanos tu duda aqui por favor : "))
            print("        GRACIAS POR PREFERIRNOS"       )

        elif(k==3):
            print("---------------------------------------") 
            print("               RECLAMOS                ")   
            print("---------------------------------------") 
            recla=str(input("Dejanos tu disgusto aqui :  "))
            print("        GRACIAS POR PREFERIRNOS"        )

        elif(k==4):
            print("---------------------------------------") 
            print("             SUGERENCIAS               ")   
            print("---------------------------------------") 
            sugr=str(input("Dejanos tu sugerencia aqui : "))
            print("        GRACIAS POR PREFERIRNOS"        ) 

        elif(k==5):
            print("---------------------------------------") 
            print("            ¡HASTA LUEGO!              ")   
            print("---------------------------------------")        


    elif (h==2):
        print("---------------------------------------") 
        print("       ¡BIENVENIDO ADMINISTRADOR!      ")   
        print("---------------------------------------") 
        print("            M E N U \n1.Crear usuario\n2.Mostrar usuarios\n3.Actualizar usuarios\n4.Eliminar usuarios\n5.Módulo de Gestión de Servicios.\n6.Módulo de Reportes.\n7.Módulo de Bonificaciones para Clientes Leales.")
        a = int(input("Elige una opcion : ")) 
        info=[]

        if (a==1):

            abrirArchivo()
            crearUsuario = {}
            crearUsuario = int(input("ingrese el numero de cedula"["cc"]))
            crearUsuario = str(input("ingrese el nombre : "["nombre"]))
            crearUsuario = input("ingrese la direccion : "["direccion"])
            crearUsuario = int(input("ingrese el numero de telefono : "["telefono"]))
            crearUsuario = str(input("ingrese la categoria a la que pertenece : "["categoria"]))

            guardarArchivo()
            info[0]["clientes"]=crearUsuario

        elif (a==2):

            print(abrirArchivo())
            for i in info[0]["clientes"]:
            
             print("***************************")
             print("nombre: " ["nombre"])
             print("Direccion : "["direccion"])
             print("Telefono :"["telefono"])
             print("Categoria : "["categoria"])
             print("***************************")

        elif (a==3):

            abrirArchivo()
            cedula=int(input("Ingrese el numero de cedula a la persona que va actualizar : "))
            
            for cedula in info:
             if cedula["cc"]==cedula:
                encontrado=True
                

            print("Qué informacion del cliente deseas actualizar : \n1.Cedula\n2.Nombre\n3.Direccion\n4.Telefono\n5.Categoria")
            b = int(input("Elige que vas a cambiar : "))
            
            if (b==1): 
                nuevaCedula = int(input("Ingresa el nuevo numero de cedula :"))
                guardarArchivo()
                info[0]["clientes"]=cedula

            elif (b==2):
                nuevoNombre = str(input("Ingresa el nuevo nombre :"))
                guardarArchivo()
                info[0]["clientes"]=nuevoNombre

            elif (b==3):
                nuevaDireccion = input("Ingresa la nueva direccion :")
                guardarArchivo()
                info[0]["clientes"]=nuevaDireccion

            elif (b==4):
                nuevoTelefono = int(input("Ingresa el nuevo numero de telefono :"))
                guardarArchivo()
                info[0]["clientes"]=nuevoTelefono

            elif (b==5):
                nuevaCategoria = str(input("Ingresa la nueva categoria :"))
                guardarArchivo()
                info[0]["clientes"].append=nuevaCategoria
            
        elif (a==4):

                abrirArchivo()

                cedula=int(input("Ingrese el numero de cedula de la persona que desea eliminar : "))
                for cedula in info:
                 if cedula["cc"]==cedula:
                    del cedula[0]["clientes"]
                    print("estudiante eliminado con exito.")      
                 else:
                    print("Cliente no encontrado.")   
 
        elif(a==5):
            print("")
        elif(a==6):
            print("")  
        elif(a==7):
            print("")    


elif(j==2):
    print("---------------------------------------") 
    print("            ¡HASTA LUEGO!              ")   
    print("---------------------------------------") 


