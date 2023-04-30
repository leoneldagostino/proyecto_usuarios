from psycopg2 import pool
import sys
from manejoLoggin import log
class Conexion:
    _DATABASE = 'datos_usuario_app_python'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5433'
    _HOST = '127.0.0.1'
    _pool = None
    _MIN = 1
    _MAX = 5    
    
    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN,cls._MAX,database = cls._DATABASE,user = cls._USERNAME,password = cls._PASSWORD,host = cls._HOST,port = cls._DB_PORT)
                log.debug(f"Creacion del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(F'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool
    
       
    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()#este metodo realizara la conexion correspondiente para que sea utilizada por el cliente
        log.debug(f'Conexcion obtenida del pool: {conexion}')
        return conexion
       
    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)#el metodo regresara la conexion al pool de conexiones para que se utilice en otro momento o otro cliente lo utilice 
        log.debug(f'Regresamos la conexion al pool: {conexion}')
        
        
    @classmethod
    def cerrar_conexion(cls):
        cls.obtener_pool().closeall()#cerrara toda las conexiones
    
    
    @classmethod
    def cerrar(cls):
        cls._cursor.close()
        cls._conexion.close()