from usuario_dao import usuario_dao
from usuario import usuario



while(True):
    print("1) Listar usuarios\n"
          "2) Agregar usuario\n" 
          "3) Actualizar usuario\n"
          "4) Eliminar usuario\n"
          "5) Salir \n")
    opcion = int(input("Ingrese la opcion que se desea seleccionar: "))
    
    match opcion:
        case 1:
            print("Opcion: 1")
            lista_usuarios = usuario_dao.seleccionar()
            for usuario in lista_usuarios:
                print(usuario)
        case 2:
            print("Opcion: 2")
            nombre = input("Ingrese el nombre de usuario: ")
            contraseña = str(input("Ingrese la contraseña del usuario: "))
            usuario_insertar = usuario(nombre,contraseña)
            usuario_dao.insertar(usuario_insertar)
        case 3:
            print("Opcion: 3")
            id_actualizacion = str(input("Ingrese el id del usuario a cambiar: "))
            nombre = input("Ingrese el nombre de usuario: ")
            contraseña = str(input("Ingrese la contraseña del usuario: "))
            usuario_actualizar = usuario(nombre,contraseña,id_actualizacion)
            usuario_dao.actualizar(usuario_actualizar)
            
        case 4:
            print("Opcion: 4")
            id_usuario_eliminar = int(input("Ingresar el id usuario que desea eliminar: "))
            usuario_eliminiar = usuario(id_usuario = id_usuario_eliminar)
            usuario_dao.eliminar(usuario_eliminiar)
            
        case 5:
            break