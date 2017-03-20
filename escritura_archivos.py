outfile = open('texto.txt', 'w') # Indicamos el valor 'w'.
outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero sobreescribiendo su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()
