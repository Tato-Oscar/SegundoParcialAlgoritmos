# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# los índices de cada uno de los árboles deben ser nombre, número y tipo;
# punto 1. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# punto 2. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# punto 3. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# punto 4. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# punto 5. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# punto 6. determinar cuantos Pokémons tienen megaevolucion.
# punto 7. determinar cuantos Pokémons tiene forma gigamax.
# cargue al menos 100 Pokémons.

from tree import BinaryTree
from pokemon_list import obtener_pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

def cargar_arboles():
    lista_pokemons = obtener_pokemons()
    
    for p in lista_pokemons:
        arbol_nombre.insert_node(p.nombre, p)
        arbol_numero.insert_node(p.numero, p)
        for tipo in p.tipos:
            nodo_tipo = arbol_tipo.search(tipo)
            if nodo_tipo:
                nodo_tipo.other_values.append(p)
            else:
                arbol_tipo.insert_node(tipo, [p])

cargar_arboles()

print("ejercicio 1")
# punto 1. busqueda por nmro y nombre
def buscar_por_numero(numero):
    nodo = arbol_numero.search(numero)
    if nodo:
        print(f"encontrado por número: {nodo.other_values}")

def buscar_por_proximidad(raiz, prefijo):
    if raiz is not None:
        buscar_por_proximidad(raiz.left, prefijo)
        if prefijo.lower() in str(raiz.value).lower():
            print(raiz.other_values)
        buscar_por_proximidad(raiz.right, prefijo)

print("\npunto 1")
# punto 1. busqueda por nmro y nombre
print("busqueda por numero y nombre")
buscar_por_numero(25)
print("busqueda por proximidad ('bul')")
buscar_por_proximidad(arbol_nombre.root, "bul")

print("\npunto 2")
# punto 2. nombres de pokemons
print("pokemones por tipo")
tipos_buscados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for t in tipos_buscados:
    nodo = arbol_tipo.search(t)
    if nodo:
        nombres = [p.nombre for p in nodo.other_values]
        print(f"Tipo {t}: {nombres}")

print("\npunto 3")
# punto 3. listados ascendentes y por nivel
def inorden_pokemon(raiz):
    if raiz is not None:
        inorden_pokemon(raiz.left)
        print(raiz.other_values)
        inorden_pokemon(raiz.right)

from queue_ import Queue
def by_level_pokemon(raiz):
    pendings = Queue()
    if raiz is not None:
        pendings.arrive(raiz)
        while pendings.size() > 0:
            nodo = pendings.attention()
            print(nodo.other_values)
            if nodo.left is not None:
                pendings.arrive(nodo.left)
            if nodo.right is not None:
                pendings.arrive(nodo.right)

print("\nlistado ascendente por número")
inorden_pokemon(arbol_numero.root)
print("\nlistado ascendente por nombre")
inorden_pokemon(arbol_nombre.root)
print("\nlistado por nivel por nombre")
by_level_pokemon(arbol_nombre.root)






print("\npunto 4")
# punto 4. debiles frente a jolteon, lycanroc y tyrantrum
print("debiles frente a jolteon, lycanroc y tyrantrum")
tipos_ataque = ["Eléctrico", "Roca", "Dragón"]
def buscar_debilidades(raiz):
    if raiz is not None:
        buscar_debilidades(raiz.left)
        poke = raiz.other_values
        if any(debilidad in tipos_ataque for debilidad in poke.debilidades):
            print(poke.nombre, "- Débil a:", poke.debilidades)
        buscar_debilidades(raiz.right)

buscar_debilidades(arbol_nombre.root)

print("\npunto 5")
# punto 5. cantidad de pokemons por tipo
print("tipos de pokemons y cantidades")
def contar_tipos(raiz):
    if raiz is not None:
        contar_tipos(raiz.left)
        print(f"tipo: {raiz.value} - cantidad: {len(raiz.other_values)}")
        contar_tipos(raiz.right)
contar_tipos(arbol_tipo.root)

print("\npunto 6 y 7")
# punto 6 y 7. cantidad de mega y gigamax
def contar_mega_giga(raiz, contadores):
    if raiz is not None:
        contar_mega_giga(raiz.left, contadores)
        if raiz.other_values.mega:  
            contadores["mega"] += 1
        if raiz.other_values.gigamax:
            contadores["giga"] += 1
        contar_mega_giga(raiz.right, contadores)

contadores = {"mega": 0, "giga": 0}
contar_mega_giga(arbol_nombre.root, contadores)
print(f"estadisticas")
print(f"megaevolucion: {contadores['mega']}")  #punto 6 indica la cantidad de mega evoluciones
print(f"forma gigamax: {contadores['giga']}")  #punto 7 indica la cantidad de gigamax