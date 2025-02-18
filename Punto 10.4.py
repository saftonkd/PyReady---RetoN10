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

def sumar_columna(matriz, columna):
  """Función para sumar los elementos de una columna"""
  suma_columna = 0
  for fila in matriz:
    suma_columna += fila[columna]
  return suma_columna

if __name__ == "__main__":
  filas = int(input("Ingrese el número de filas de la matriz: "))
  columnas = int(input("Ingrese el número de columnas de la matriz: "))
  matriz = matriz(filas, columnas)
  columna = int(input(f"Ingrese el número de la columna a sumar (0-{columnas-1}): ")) # Columna que se desea sumar
  if columna < 0 or columna >= columnas:  # Validar que el índice de columna corresponda con el de la matriz
    print("El número de columna es inválido")
  else:
    suma_columna = sumar_columna(matriz, columna)
    print(f"La suma de los elementos de la columna es: {suma_columna}")
