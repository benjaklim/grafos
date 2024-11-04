import heapq

ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

grafo = {
    "cocina": [("comedor", 5), ("baño 1", 8), ("terraza", 10)],
    "comedor": [("cocina", 5), ("sala de estar", 6), ("baño 2", 9), ("quincho", 7)],
    "cochera": [("terraza", 12), ("habitación 1", 15), ("baño 1", 7)],
    "quincho": [("patio", 5), ("baño 2", 6), ("cocina", 4)],
    "baño 1": [("cocina", 8), ("baño 2", 3), ("habitación 1", 10), ("terraza", 6)],
    "baño 2": [("comedor", 9), ("quincho", 6), ("baño 1", 3)],
    "habitación 1": [("cochera", 15), ("baño 1", 10), ("habitación 2", 5)],
    "habitación 2": [("habitación 1", 5), ("sala de estar", 8)],
    "sala de estar": [("comedor", 6), ("habitación 2", 8), ("terraza", 7)],
    "terraza": [("cocina", 10), ("cochera", 12), ("baño 1", 6), ("sala de estar", 7), ("patio", 9)],
    "patio": [("quincho", 5), ("terraza", 9)]
}

def arbol_expansion_minima(grafo, inicio):
    visitados = set([inicio])
    aristas = [
        (peso, inicio, destino) for destino, peso in grafo[inicio]
    ]
    heapq.heapify(aristas)
    mst = []
    cable_total = 0

    while aristas and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(aristas)
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origen, destino, peso))
            cable_total += peso

            for siguiente, p in grafo[destino]:
                if siguiente not in visitados:
                    heapq.heappush(aristas, (p, destino, siguiente))

    return mst, cable_total

def camino_mas_corto(grafo, inicio, objetivo):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    anterior = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            break

        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                anterior[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    camino = []
    nodo = objetivo
    while nodo:
        camino.insert(0, nodo)
        nodo = anterior[nodo]

    return camino, distancias[objetivo]

mst, cable_total_mst = arbol_expansion_minima(grafo, "cocina")
print("Árbol de Expansión Mínima (MST):")
for (u, v, peso) in mst:
    print(f"{u} - {v}: {peso} metros")
print(f"\nTotal de metros de cable para conectar todos los ambientes: {cable_total_mst} metros")

camino_corto, distancia_camino_corto = camino_mas_corto(grafo, "habitación 1", "sala de estar")
print(f"\nCamino más corto desde habitación 1 hasta sala de estar: {camino_corto}")
print(f"Distancia del camino más corto (metros de cable): {distancia_camino_corto} metros")
