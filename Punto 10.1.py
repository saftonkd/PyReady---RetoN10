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

def sumar_matrices(primera_matriz: list, segunda_matriz: list)-> list:
  """Función para sumar dos matrices"""
  filas, columnas = len(primera_matriz), len(primera_matriz[0])
  matriz_suma = [[primera_matriz[i][j] + segunda_matriz[i][j] for j in range(columnas)] for i in range(filas)]
  return matriz_suma

def restar_matrices(primera_matriz: list, segunda_matriz: list)-> list:
  """Función para restar dos matrices"""
  filas, columnas = len(primera_matriz), len(primera_matriz[0])
  matriz_suma = [[primera_matriz[i][j] - segunda_matriz[i][j] for j in range(columnas)] for i in range(filas)]
  return matriz_suma

if __name__ == "__main__":
  filas = int(input("Ingrese el número de filas: "))
  columnas = int(input("Ingrese el número de columnas: "))
  print("Ingrese los valores de la primera matriz:")
  primera_matriz = matriz(filas, columnas)
  print("Ingrese los valores de la segunda matriz:")
  segunda_matriz = matriz(filas, columnas)
  print("Suma de matrices:")
  for i in range(len(sumar_matrices(primera_matriz, segunda_matriz))):
    print((sumar_matrices(primera_matriz, segunda_matriz))[i])
  print("Resta de matrices:")
  for i in range(len(restar_matrices(primera_matriz, segunda_matriz))):
    print((restar_matrices(primera_matriz, segunda_matriz))[i])
  
