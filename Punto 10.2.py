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

def producto_matrices(primera_matriz, segunda_matriz):
  """Función para multiplicar dos matrices"""
  filas_primera_matriz = len(primera_matriz)
  columnas_primera_matriz = len(primera_matriz[0])
  columnas_segunda_matriz = len(segunda_matriz[0])
  matriz_producto = [[0 for a in range(columnas_segunda_matriz)] for b in range(filas_primera_matriz)] # Crear la estrctura de la matriz producto con ceros
  for i in range(filas_primera_matriz):     # Calcular el producto de las matrices
    for j in range(columnas_segunda_matriz):
      for k in range(columnas_primera_matriz):
        matriz_producto[i][j] += primera_matriz[i][k] * segunda_matriz[k][j]
  return matriz_producto

if __name__ == "__main__":
  # Ingresar el número de filas y columnas de la primera matriz
  filas_primera_matriz = int(input("Ingrese el número de filas: "))
  columnas_primera_matriz = int(input("Ingrese el número de columnas: "))
  print("Ingrese los valores de la primera matriz:")
  primera_matriz = matriz(filas_primera_matriz, columnas_primera_matriz)

  # Ingresar el número de filas y columnas de la segunda matriz
  filas_segunda_matriz = int(input("Ingrese el número de filas: "))
  columnas_segunda_matriz = int(input("Ingrese el número de columnas: "))
  print("Ingrese los valores de la segunda matriz:")
  segunda_matriz = matriz(filas_segunda_matriz, columnas_segunda_matriz)

  # Calcular el producto de las matrices
  print("Producto de matrices")
  for i in range(len(producto_matrices(primera_matriz, segunda_matriz))):
    print((producto_matrices(primera_matriz, segunda_matriz))[i])


  
