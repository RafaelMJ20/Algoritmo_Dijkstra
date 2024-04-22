import heapq

class Nodo:
    def __init__(self, estado, distancia, camino):
        self.estado = estado
        self.distancia = distancia
        self.camino = camino

    # Comparación de nodos basada en la distancia
    def __lt__(self, otro):
        return self.distancia < otro.distancia

def dijkstra(estado_inicial, objetivo, graf):
    nodos_frontera = []
    heapq.heappush(nodos_frontera, Nodo(estado_inicial, 0, [estado_inicial]))
    nodos_visitados = set()

    while nodos_frontera:
        nodo_actual = heapq.heappop(nodos_frontera)

        if nodo_actual.estado == objetivo:
            return nodo_actual.camino, nodo_actual.distancia

        if nodo_actual.estado in nodos_visitados:
            continue

        nodos_visitados.add(nodo_actual.estado)

        for hijo, distancia in graf[nodo_actual.estado].items():
            if hijo not in nodos_visitados:
                nueva_distancia = nodo_actual.distancia + distancia
                nuevo_camino = nodo_actual.camino + [hijo]
                heapq.heappush(nodos_frontera, Nodo(hijo, nueva_distancia, nuevo_camino))

    return None, None

# Grafo
grafo = {
    'EDO.MEX': {'SLP': 513, 'CDMX': 125},
    'CDMX': {'SLP': 423, 'MICHOACAN': 491},
    'SLP': {'MICHOACAN': 355, 'SONORA': 603, 'MONTERREY': 313, 'GUADALAJARA': 437, 'HIDALGO': 599, 'QRO': 203, 'PUEBLA': 514},
    'MICHOACAN': {'SONORA': 346, 'MONTERREY': 296},
    'QRO': {'HIDALGO': 390},
    'MONTERREY': {'SONORA': 296},
    'GUADALAJARA': {'MONTERREY': 394, 'SLP': 437},
    'SONORA': {'MICHOACAN': 346, 'SLP': 603, 'MONTERREY': 296},
    'HIDALGO': {'SLP': 599, 'QRO': 390},
    'PUEBLA': {'SLP': 514}
}

estado_inicial = 'CDMX'
objetivo = 'SONORA'

camino, distancia = dijkstra(estado_inicial, objetivo, grafo)

if camino:
    print("Camino:", camino)
    print("Distancia:", distancia)
else:
    print("No se encontró un camino desde {} hasta {}.".format(estado_inicial, objetivo))
