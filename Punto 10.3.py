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

def matriz_transpuesta(matriz):
  """Función para obtener la matriz transpuesta de una matriz ingresada"""
  filas = len(matriz)
  columnas = len(matriz[0])
  matriz_transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]    # Crear la matriz transpuesta
  return matriz_transpuesta

if __name__ == "__main__":
  filas = int(input("Ingrese el número de filas: "))
  columnas = int(input("Ingrese el número de columnas: "))
  print("Ingrese los valores de la matriz:")
  matriz = matriz(filas, columnas)
  print("La matriz transpuesta es: ")
  for i in range(len(matriz_transpuesta(matriz))):
    print(matriz_transpuesta(matriz)[i])
