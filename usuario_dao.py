from manejoLoggin import log
from usuario import usuario
from cursor_pool import *

class usuario_dao:
    _SELECIONAR = 'SELECT * FROM tabla_usuario '
    _INSERTAR = ' INSERT INTO tabla_usuario(username,contraseña) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE tabla_usuario SET username = %s, contraseña = %s  WHERE id_usuario = %s'
    _ELMINIAR = 'DELETE FROM tabla_usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
        sentencia = cls._SELECIONAR       
        with cursor_pool() as cursor:
            cursor.execute(sentencia)   
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario_registro = usuario(user_name = registro[1], password = registro[2],id_usuario = registro[0])
                usuarios.append(usuario_registro)
            return usuarios
            
    @classmethod
    def insertar(cls,usuario):
        sentencia = cls._INSERTAR
        datos = (usuario.user_name, usuario.password)
        with cursor_pool() as cursor:
            cursor.execute(sentencia,datos)
            log.debug("Datos insertados correctamente")
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,usuario):
        sentencia = cls._ACTUALIZAR
        with cursor_pool() as cursor:
            datos = (usuario.user_name,usuario.password,usuario.id_usuario)
            cursor.execute(sentencia,datos)
            log.debug(f"persona actualizada {usuario}")
            return cursor.rowcount
              
    @classmethod
    def eliminar(cls,usuario):
        sentencia = cls._ELMINIAR
        with cursor_pool() as cursor:
            dato = (usuario.id_usuario,)
            cursor.execute(sentencia,dato)
            log.debug(f"Persona eliminada {usuario}")
            return cursor.rowcount
        

