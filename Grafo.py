import time
from collections import deque
from Nodo import Nodo
from Arista import Arista

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.ady = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)
            self.ady[nombre] = []

    def agregar_arista(self, origen, destino):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.ady[origen].append(destino)

    # BFS

    def bfs(self, inicio, meta):
        start = time.time()

        visitado = set([inicio])
        cola = deque([inicio])
        padres = {inicio: None}
        dist = {inicio: 0}

        while cola:
            actual = cola.popleft()

            if actual == meta:
                break

            for vecino in self.ady[actual]:
                if vecino not in visitado:
                    visitado.add(vecino)
                    padres[vecino] = actual
                    dist[vecino] = dist[actual] + 1
                    cola.append(vecino)

        # reconstruir ruta
        ruta = []
        if meta in padres:
            nodo = meta
            while nodo is not None:
                ruta.append(nodo)
                nodo = padres[nodo]
            ruta.reverse()

        arbol = self._arbol(padres)
        tiempo = time.time() - start

        return dist, padres, ruta, arbol, tiempo


    #DFS estilo académico

    def dfs(self, inicio, meta):
        visited = {nodo: False for nodo in self.ady}
        padres = {inicio: None}
        recorrido = []
        ruta_encontrada = []

        print("\n=== Iniciando DFS ===\n")

        # ---- función recursiva ----
        def _dfs(nodo):
            visited[nodo] = True
            recorrido.append(nodo)

            print(f"Visitando: {nodo}")
            print("Vecinos de", nodo, ":", self.ady[nodo])
            print()

            if nodo == meta:
                return True

            for vecino in self.ady[nodo]:
                if not visited[vecino]:
                    padres[vecino] = nodo
                    
                    if _dfs(vecino):   # llamada recursiva
                        return True

                    print("Finaliza", vecino)
                    print("Vuelve a", nodo)
                    print()

            return False

        _dfs(inicio)

        # reconstrucción de ruta
        if visited[meta]:
            nodo = meta
            while nodo is not None:
                ruta_encontrada.append(nodo)
                nodo = padres[nodo]
            ruta_encontrada.reverse()

        arbol = self._arbol(padres)

        return padres, ruta_encontrada, recorrido, arbol, visited


    # Auxiliar árbol

    def _arbol(self, padres):
        arbol = {}
        for hijo, padre in padres.items():
            if padre is not None:
                arbol.setdefault(padre, []).append(hijo)
        return arbol

    def mostrar_salas(self):
        return list(self.nodos.keys())

    def mostrar_conexiones(self):
        print("\nConexiones del hospital (Grafo):")
        for origen, destinos in self.ady.items():
            print(f"{origen} → {destinos}")
