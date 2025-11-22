from Grafo import Grafo

# ==========================
#  CREAR EL GRAFO DEL HOSPITAL
# ==========================
g = Grafo()

g.agregar_arista("PasilloA", "Laboratorio")
g.agregar_arista("PasilloA", "RayosX")
g.agregar_arista("PasilloA", "Odontologia")
g.agregar_arista("PasilloA", "PasilloB")
g.agregar_arista("Laboratorio", "PasilloA")
g.agregar_arista("RayosX", "PasilloA")
g.agregar_arista("Odontologia", "PasilloA")
g.agregar_arista("PasilloB", "Pediatria")
g.agregar_arista("PasilloB", "Cirugia")
g.agregar_arista("Pediatria", "PasilloB")
g.agregar_arista("Cirugia", "PasilloB")
g.agregar_arista("PasilloB", "PasilloA")
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
