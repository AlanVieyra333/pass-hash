from optparse import OptionParser
import hashlib

LENGHT = 12

def generar_hash(texto):
  """
  Genera un hash de un texto.

  Args:
    texto: El texto a hashear.

  Returns:
    El hash del texto.
  """

  # Convertimos el texto a bytes.
  texto_bytes = texto.encode("utf-8")

  # Creamos un objeto hash SHA-256.
  hash_sha256 = hashlib.sha256()

  # Agregamos el texto al objeto hash.
  hash_sha256.update(texto_bytes)

  # Obtenemos el hash del objeto.
  hash_digest = hash_sha256.digest()

  # Convertimos el hash a una cadena de texto.
  hash_string = hash_digest.hex()

  # recorremos el hash para que inicie con una letra
  for i in range(len(hash_string)):
    if hash_string[i].isalpha():
      hash_string = hash_string[i:]
      break

  # Recortamos el hash a 'n' caracteres.
  hash_string = hash_string[:(LENGHT-1)]

  # Agregamos una letra mayuscula al hash.
  for i in range(1,len(hash_string)):
    if hash_string[i].isalpha():
      hash_string = hash_string[:i] + hash_string[i].upper() + hash_string[i+1:]
      break

  # Agregamos un caracter especial al hash.
  hash_string += "%"

  return hash_string

if __name__ == "__main__":
  usage = "%prog [options] <text>"
  parser = OptionParser(usage=usage, add_help_option=False)
  parser.add_option("-h", "--help", action="help",
      help=u"proceso para hashear un texto con caracteristicas de una contrasenia")
  (options, args) = parser.parse_args()

  if len(args) == 0:
      parser.error("Se tiene que indicar el texto que se desa hashear. (Eg. pass:page)")
  else:
      text = args[0]

  # Generamos el hash.
  hash_string = generar_hash(text)

  # Imprimimos el hash.
  print("Password with %d characters: %s" % (LENGHT,hash_string))