# Ejercicio 2: 
# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# punto 1: hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# punto 2: determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
#  cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# punto 3: calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# punto 4: indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph
from starwars_list import obtener_personajes, obtener_conexiones


g_sw = Graph(is_dir=False)


for p, total_eps in obtener_personajes():
    g_sw.add_vertex(p, other_values={"eps_totales": total_eps})


for peso, origen, destino in obtener_conexiones():
    g_sw.add_edge(peso, origen, destino)

print("\npunto 1")
# ounto 1. arbol de expansion minimo (Kruskal) desde C-3PO, Yoda y Leia
print("arbol de expansion minimo")
for inicio in ["C-3PO", "Yoda", "Leia"]:
    print(f"\narbol de expansion minimo {inicio}:")
    mst = g_sw.kruskal(inicio)
    print(mst)

print("\npunto 2")
# punto 2. numero maximo de episodios compartidos y que pares lo comparten
max_eps = 0
pares_max = []

for vertice in g_sw:
    for arista in vertice.edges:
        if arista.weight > max_eps:
            max_eps = arista.weight
            pares_max = [frozenset([vertice.value, arista.destination])]
        elif arista.weight == max_eps:
            par = frozenset([vertice.value, arista.destination])
            if par not in pares_max:
                pares_max.append(par)

print(f"\nnumero maximo de episodios compartidos: {max_eps}")
for par in pares_max:
    print(list(par))


print("\npunto 3")
# punto 3. caminos mas cortos (Dijkstra)
def mostrar_camino_mas_corto(grafo, origen, destino):
    print(f"\ncamino mas corto de {origen} a {destino}:")
    if grafo.exist_path(origen, destino):
        paths = grafo.dijkstra(origen)
        destino_actual = destino
        peso_total = None
        camino = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destino_actual:
                if peso_total is None:
                    peso_total = value[1]
                camino.append(value[0])
                destino_actual = value[2]
        camino.reverse()
        print(f"ruta: {' -> '.join(camino)} | costo total (episodios sumados): {peso_total}")
    else:
        print("no existe un camino")

mostrar_camino_mas_corto(g_sw, "C-3PO", "R2-D2")
mostrar_camino_mas_corto(g_sw, "Yoda", "Darth Vader")

print("\npunto 4")
# punto 4. personajes que aparecieron en los nueve episodios
print("personajes que aparecieron en los 9 episodios")
for vertice in g_sw:
    if vertice.other_values["eps_totales"] == 9:
        print(vertice.value)