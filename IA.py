matriz = [["","",""],["","",""],["","",""]]

def gato(matriz):
    coordenadas = input("Indique las coordenada (1,1): ")
    coordenadasl = coordenadas.split(",")
    
    
def action(matriz):
    posiciones = []
    for i in range(3):
        for j in range(3):
          if (matriz[i][j] == ""):
              posiciones += [[i,j]]
    return posiciones
