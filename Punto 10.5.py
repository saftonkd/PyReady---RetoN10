def matriz(filas: int, columnas: int)-> list:
  """Función para crear una matriz con valores ingresados"""
  matriz : list = []
  for i in range(filas):
    fila : list = []
    for j in range(columnas):
      elemento = float(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
      fila.append(elemento)
    matriz.append(fila)
  return matriz

def sumar_fila(matriz, fila):
    """Función para sumar los elementos de una fila"""
    suma_fila = 0
    for valor in matriz[fila]:
        suma_fila += valor
    return suma_fila

if __name__ == "__main__":
  filas = int(input("Ingrese el número de filas de la matriz: "))
  columnas = int(input("Ingrese el número de columnas de la matriz: "))
  print("Ingrese los valores de la matriz:")
  matriz = matriz(filas, columnas)
  fila = int(input(f"Ingrese el número de la fila a sumar (0-{filas-1}): ")) # Solicitar la fila para sumar
  if fila < 0 or fila >= filas:
    print("El número de fila es inválido") # Validar que el índice de columna corresponda con el de la matriz
  else:
    suma_fila = sumar_fila(matriz, fila)
    print(f"La suma de los elementos de la fila {fila} es: {suma_fila}")
