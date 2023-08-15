from collections import deque
import time
import copy

somador = 0
for i in range (0, 10):
    tempoInicio = time.time()
    def viajar(portoPartida, portoDestino, mapa):
        vizinhos1 = deque([])
        vizinhos2 = deque([])
        vizinhos1.append(portoPartida)
        distancia = 0
        while vizinhos1 or vizinhos2:
            while vizinhos1:
                atual = vizinhos1.popleft()
                pegarVizinhos(atual, vizinhos2, mapa)
            if mapa[portoDestino[0]][portoDestino[1]] is True:
                return distancia + 1
            while vizinhos2:
                atual = vizinhos2.popleft()
                pegarVizinhos(atual, vizinhos1, mapa)
            if mapa[portoDestino[0]][portoDestino[1]] is True:
                return distancia + 2
            distancia += 2
        return 0

    def pegarVizinhos(coordenada, lista, mapa):
            if coordenada[0] != 0:
                if mapa[coordenada[0]-1][coordenada[1]] is False:
                    mapa[coordenada[0]-1][coordenada[1]] = True
                    lista.append([coordenada[0]-1, coordenada[1]])
            if coordenada[0] + 1 < latitudeMatriz:
                if mapa[coordenada[0]+1][coordenada[1]] is False:
                    mapa[coordenada[0]+1][coordenada[1]] = True
                    lista.append([coordenada[0]+1, coordenada[1]])
            if coordenada[1] != 0:
                if mapa[coordenada[0]][coordenada[1]-1] is False:
                    mapa[coordenada[0]][coordenada[1]-1] = True
                    lista.append([coordenada[0], coordenada[1]-1])
            if coordenada[1] + 1 < longitudeMatriz:
                if mapa[coordenada[0]][coordenada[1]+1] is False:
                    mapa[coordenada[0]][coordenada[1]+1] = True
                    lista.append([coordenada[0], coordenada[1]+1])

    arquivo = 'caso20.txt'
    with open("casos/" + arquivo) as f:

        dimensoes = f.readline().split(" ")
        latitudeMatriz = int(dimensoes[0])
        longitudeMatriz = int(dimensoes[1])
        latitudePonto = 0
        longitudePonto = 0
        coordenadasPontos = [0] * 9
        mapaOriginal = []
        listaLinha = []

        print("\nExecutando arquivo: " + arquivo)
        for linha in f.readlines():
            for coordenada in linha:
                if coordenada.isdigit():
                        coordenadasPontos[int(coordenada) - 1] = [latitudePonto, longitudePonto]

                if coordenada == '*':
                    listaLinha.append(None)
                else:
                    listaLinha.append(False)
                longitudePonto += 1

            mapaOriginal.append(listaLinha)
            listaLinha = []
            latitudePonto += 1
            longitudePonto = 0

        totalCombustivel = 0
        mapaCopia = copy.deepcopy(mapaOriginal)

        for i in range(0, len(coordenadasPontos)):
            proximo = (i+1)%9
            resultado = viajar(coordenadasPontos[i], coordenadasPontos[proximo], mapaCopia)

            if(resultado == 0):
                doisAFrente = (i+2)%9
                mapaCopia = copy.deepcopy(mapaOriginal)
                resultado = viajar(coordenadasPontos[i], coordenadasPontos[doisAFrente], mapaCopia)
            totalCombustivel += resultado
            mapaCopia = copy.deepcopy(mapaOriginal)

        print('Combustível total: ' + str(totalCombustivel))
        segundos = (time.time() - tempoInicio)
        print(str(int(segundos / 60)) + " minuto(s) e " + str(segundos % 60) + " segundo(s).")
        somador += segundos

print("\n" + "-" * 50)
print("O tempo de 10 execuções é " + str(somador/10))
        