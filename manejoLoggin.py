import logging as log 

'''
manda informacion a nuestra consola en distintos niveles dependiendo de los mismos

normalmente en productos en produccion es apartir del nivel warning

asctime agrega el tiempo(en fecha y hora) en el log
levelname muestra que tipo de nivel
filename muestra el archivo que arroja el mensaje del log
lineno muestra el numero de la linea que da error
message muestra el mensaje que agregamos al log

datefmt dara formato de hora 

fileHandler crea un archivo con los logs de la consola

'''
log.basicConfig(level=log.DEBUG
                ,format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s \n',
                datefmt='%I: %M: %S %p',
                handlers=[
                    log.FileHandler('datos.log'),
                    log.StreamHandler()
                ])

# log.debug("Mensaje nivel debug")
# log.info("Mensaje nivel info")
# log.warning("Mensaje nivel warning")
# log.error("Mensaje nivel error")
# log.critical("Mensaje nivel critical")