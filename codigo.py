import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1][vertice2] = peso
            self.vertices[vertice2][vertice1] = peso

    def dijkstra(self, inicio):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        visitados = set()
        heap = [(0, inicio)]

        while heap:
            (distancia, vertice_actual) = heapq.heappop(heap)

            if vertice_actual in visitados:
                continue

            visitados.add(vertice_actual)

            for vecino, peso in self.vertices[vertice_actual].items():
                distancia_nueva = distancia + peso

                if distancia_nueva < distancias[vecino]:
                    distancias[vecino] = distancia_nueva
                    heapq.heappush(heap, (distancia_nueva, vecino))

        return distancias

# Crear el grafo
grafo = Grafo()
vertices = [1, 2, 3, 4, 5, 6, 7]

for vertice in vertices:
    grafo.agregar_vertice(vertice)

aristas = [
    (1, 2, 3), (1, 3, 6),
    (2, 3, 2), (2, 4, 1),
    (3, 4, 4), (3, 5, 2),
    (4, 5, 6), (5, 6, 2),
    (5, 7, 2), (6, 7, 3)
]

for arista in aristas:
    grafo.agregar_arista(*arista)

# Calcular el camino más corto desde el vertice 1 al vertice 7
inicio = 1
distancias = grafo.dijkstra(inicio)

# Encontrar el camino
destino = 7
camino = [destino]
while destino != inicio:
    for vertice, peso in grafo.vertices[destino].items():
        if distancias[destino] - peso == distancias[vertice]:
            camino.append(vertice)
            destino = vertice
            break

camino.reverse()
print("Camino más corto desde el vertice 1 al vertice 7:", ' -> '.join(map(str, camino)))
