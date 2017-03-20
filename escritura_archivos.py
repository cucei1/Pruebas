outfile = open('nombrearchivo.txt', 'w') # Indicamos el valor 'w'.
outfile.write('Linea del archivo de texto plano\n') #con salto de linea
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero sobreescribiendo su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()
