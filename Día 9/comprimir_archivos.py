# Descomprimir archivos
import shutil
import zipfile
archivo_comprimido = 'carpeta.zip'

destino = 'Proyecto'

shutil.unpack_archive('carpeta.zip',destino, 'zip')
print('se ha descomprimido')