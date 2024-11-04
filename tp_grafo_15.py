import heapq
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.maravillas = {}
    
    def agregar_maravilla(self, nombre, paises):
        self.maravillas[nombre] = {
            'paises': paises,
            'tipo': 'natural'
        }

    def agregar_arista(self, nombre1, nombre2, distancia):
        self.grafo[nombre1].append((nombre2, distancia))
        self.grafo[nombre2].append((nombre1, distancia))

    def arbol_expansion_minima(self):
        visitados = set()
        mst = []
        cable_total = 0

        inicio = next(iter(self.maravillas))
        aristas = [(distancia, inicio, destino) for destino, distancia in self.grafo[inicio]]
        heapq.heapify(aristas)
        visitados.add(inicio)

        while aristas and len(visitados) < len(self.maravillas):
            distancia, origen, destino = heapq.heappop(aristas)
            if destino not in visitados:
                visitados.add(destino)
                mst.append((origen, destino, distancia))
                cable_total += distancia

                for siguiente, dist in self.grafo[destino]:
                    if siguiente not in visitados:
                        heapq.heappush(aristas, (dist, destino, siguiente))

        return mst, cable_total

    def pais_con_multiples_maravillas(self):
        maravillas_por_pais = defaultdict(int)
        for maravilla, datos in self.maravillas.items():
            for pais in datos['paises']:
                maravillas_por_pais[pais] += 1
        return [pais for pais, count in maravillas_por_pais.items() if count > 1]

grafo = Grafo()

grafo.agregar_maravilla("Amazonas", ["Brasil", "Perú", "Colombia"])
grafo.agregar_maravilla("Bahía de Ha Long", ["Vietnam"])
grafo.agregar_maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"])
grafo.agregar_maravilla("Isla Jeju", ["Corea del Sur"])
grafo.agregar_maravilla("Komodo", ["Indonesia"])
grafo.agregar_maravilla("Río Subterráneo de Puerto Princesa", ["Filipinas"])
grafo.agregar_maravilla("Montaña de la Mesa", ["Sudáfrica"])

grafo.agregar_arista("Amazonas", "Bahía de Ha Long", 17000)
grafo.agregar_arista("Amazonas", "Cataratas del Iguazú", 3200)
grafo.agregar_arista("Amazonas", "Isla Jeju", 15500)
grafo.agregar_arista("Amazonas", "Komodo", 13000)
grafo.agregar_arista("Amazonas", "Río Subterráneo de Puerto Princesa", 17500)
grafo.agregar_arista("Amazonas", "Montaña de la Mesa", 7500)
grafo.agregar_arista("Bahía de Ha Long", "Cataratas del Iguazú", 17000)
grafo.agregar_arista("Bahía de Ha Long", "Isla Jeju", 3000)
grafo.agregar_arista("Bahía de Ha Long", "Komodo", 4000)
grafo.agregar_arista("Bahía de Ha Long", "Río Subterráneo de Puerto Princesa", 1700)
grafo.agregar_arista("Bahía de Ha Long", "Montaña de la Mesa", 13000)
grafo.agregar_arista("Cataratas del Iguazú", "Isla Jeju", 18000)
grafo.agregar_arista("Cataratas del Iguazú", "Komodo", 16000)
grafo.agregar_arista("Cataratas del Iguazú", "Río Subterráneo de Puerto Princesa", 19000)
grafo.agregar_arista("Cataratas del Iguazú", "Montaña de la Mesa", 8000)
grafo.agregar_arista("Isla Jeju", "Komodo", 3000)
grafo.agregar_arista("Isla Jeju", "Río Subterráneo de Puerto Princesa", 2400)
grafo.agregar_arista("Isla Jeju", "Montaña de la Mesa", 15000)
grafo.agregar_arista("Komodo", "Río Subterráneo de Puerto Princesa", 1700)
grafo.agregar_arista("Komodo", "Montaña de la Mesa", 12000)
grafo.agregar_arista("Río Subterráneo de Puerto Princesa", "Montaña de la Mesa", 14000)

mst_natural, cable_total_natural = grafo.arbol_expansion_minima()
print("Árbol de Expansión Mínima - Maravillas Naturales:")
for (u, v, peso) in mst_natural:
    print(f"{u} - {v}: {peso} km")
print(f"Total de distancia para conectar todas las maravillas naturales: {cable_total_natural} km\n")

paises_multiples_maravillas = grafo.pais_con_multiples_maravillas()
print("Países con múltiples maravillas naturales:", paises_multiples_maravillas)
