from manejoLoggin import log
from base_datos import Conexion

class cursor_pool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_excepcion,valor_excep,detalle_except):
        if valor_excep:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_excep} - {tipo_excepcion} - {detalle_except}')
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)
        
