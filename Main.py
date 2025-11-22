from Grafo import Grafo

# ==========================
#  CREAR EL GRAFO DEL HOSPITAL
# ==========================
g = Grafo()

g.agregar_arista("Patient", "HallA")
g.agregar_arista("HallA", "HallB")
g.agregar_arista("HallB", "XRay")
g.agregar_arista("HallA", "Lab")
g.agregar_arista("Lab", "Pharmacy")
g.agregar_arista("HallB", "Surgery")
g.agregar_arista("Surgery", "IntensiveCare")

# ==========================
#    MENÚ DE USUARIO
# ==========================
print("========== HOSPITAL MAPA ==========")
print("Salas del hospital:\n")

for sala in g.mostrar_salas():
    print(" -", sala)

g.mostrar_conexiones()

print("\n====================================")
inicio = input("\nIngrese la sala donde se encuentra el paciente: ").strip()
meta = input("Ingrese a dónde quiere ir (ej: XRay): ").strip()

# ==========================
#   MOSTRAR CONEXIONES
# ==========================


print("\n====================================")
inicio = input("\nIngrese la sala donde se encuentra el paciente: ").strip()
meta = input("Ingrese a dónde quiere ir (ej: XRay): ").strip()

# ==========================
#      EJECUTAR BFS
# ==========================
print("\n\n============= BFS =============")
dist, padres_bfs, ruta_bfs, arbol_bfs, t_bfs = g.bfs(inicio, meta)

print("Ruta más corta:", ruta_bfs)
print("Árbol BFS:", arbol_bfs)
print("Tiempo:", t_bfs)


# ==========================
#      EJECUTAR DFS
# ==========================
print("\n\n============= DFS =============")
padres_dfs, ruta_dfs, rec_dfs, arbol_dfs, t_dfs = g.dfs(inicio, meta)

print("Ruta DFS:", ruta_dfs)
print("Recorrido DFS:", rec_dfs)
print("Árbol DFS:", arbol_dfs)
print("Tiempo:", t_dfs)
