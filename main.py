import random 
import tablero as tab

def generarTablero(dimension):
    tablero = []
    for _ in range(dimension):
        fila = [0 for _ in range(dimension)]
        index = random.randint(0, dimension-1)
        fila[index] = 1
        tablero.append(fila)
    return tablero

def encontrarReinas(tablero, n):
    reinas = []
    for i in range(n):
        for j in range(n):
            celda = tablero[i][j]
            if celda == 1:
                reinas.append((i,j))
    return reinas

def recorrerDireccion(tablero, n, i, j, l, m):
    ataques = []
    while True:
        i += l
        j += m
        continuar = j >= 0 and j <= n-1 and i >= 0 and i <= n-1
        if not continuar:
            break
        celda = tablero[i][j]
        if celda == 1:
            ataques.append((i,j))
    return ataques

def recorrerDiagonal1(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, -1, 1)
    
def recorrerDiagonal2(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, -1, -1)
    
def recorrerDiagonal3(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, 1, 1)
    
def recorrerDiagonal4(tablero, n, i, j):
   return recorrerDireccion(tablero, n, i, j, 1, -1)

def recorrerArriba(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, -1, 0)

def recorrerAbajo(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, +1, 0)

def recorrerDerecha(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, 0, 1)

def recorrerIzquierda(tablero, n, i, j):
    return recorrerDireccion(tablero, n, i, j, 0, -1)

def agregarEncontrados(ataques, encontrados):
    if len(encontrados) > 0:
        ataques.extend(encontrados)

def encontrarAtaques(tablero, dimension, i, j):
    ataques = []
    resp = recorrerDiagonal1(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerDiagonal2(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerDiagonal3(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerDiagonal4(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerArriba(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerAbajo(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerDerecha(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    resp = recorrerIzquierda(tablero, dimension, i, j)
    agregarEncontrados(ataques, resp)
    
    return ataques

def generarPoblacion(dimension, cantidad):
    poblacion = []
    for _ in range(cantidad):
        individuo = generarTablero(dimension)
        poblacion.append(individuo)
    return poblacion

def extraerPoblacion(poblacion, cantidadExtraer):
    seleccionados = []
    for _ in range(cantidadExtraer):
        index = random.randint(0, len(poblacion)-1)
        seleccionado = poblacion[index]
        seleccionados.append(seleccionado)
        del poblacion[index]
    return seleccionados
        

def funcionAptitud(individuo, dimension):
    reinas = encontrarReinas(individuo, dimension)
    total = 0
    for reina in reinas:
        ataques = encontrarAtaques(individuo, dimension, reina[0], reina[1])
        total += len(ataques)
    individuoPuntuado = (individuo, total)
    return individuoPuntuado

def puntuarIndiviuos(individuos, dimension):
    puntuados = []
    for individuo in individuos:
        puntuado = funcionAptitud(individuo, dimension)
        puntuados.append(puntuado)
    return puntuados
    
def seleccion(individuosPuntuados):
    # ruleta = [0 for i in range(100)] 
    sumaPuntos = 0
    for puntuado in individuosPuntuados:
        sumaPuntos += puntuado[1]
    candidatos = []
    for puntuado in individuosPuntuados:
        probabilidad = 1 - puntuado[1] / sumaPuntos
        candidatos.append((puntuado[0], puntuado[1], probabilidad))
    candidatos = sorted(candidatos, key = lambda c: c[2], reverse=True)
    seleccionados = []
    for candidato in candidatos:
        puntero = random.random()
        probabilidad = candidato[2]
        if puntero <= probabilidad:
            seleccionados.append(candidato[0])
        if len(seleccionados) == 2:
            break
    return seleccionados

def cruzamiento(padres):
    femenino = padres[0]
    masculino = padres[1]
    corte = random.randint(1, len(femenino)-1)
    hijo1 = femenino[:corte]
    hijo1.extend(masculino[corte:])
    pass
    

dimension = 4
tamanioPoblacion = 20
tamanioSubpoblacion = 4
poblacionInicial = generarPoblacion(dimension, tamanioPoblacion)
subpoblacion = extraerPoblacion(poblacionInicial, tamanioSubpoblacion)
puntuados = puntuarIndiviuos(subpoblacion, dimension)
padres = seleccion(puntuados)
hijos = cruzamiento(padres)
print(funcionAptitud(poblacionInicial[0], dimension))
# tab.guardar(poblacionInicial[0], 'original.svg', dimension)