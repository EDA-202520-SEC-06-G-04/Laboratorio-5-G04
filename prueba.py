from DataStructures.List import single_linked_list as sll

def default_sort_criteria(a, b):
    return a < b

# Crear lista desordenada original
lista_original = sll.new_list()
sll.add_last(lista_original, 1)
sll.add_last(lista_original, 2)

# Funciones de ordenamiento a probar
sort_functions = ["selection_sort", "insertion_sort", "shell_sort", "merge_sort", "quick_sort"]

for sort_func in sort_functions:
    # Clonar la lista antes de ordenar
    lista_copia = sll.new_list()
    node = lista_original["first"]
    while node:
        sll.add_last(lista_copia, node["info"])
        node = node["next"]

    print(f"\n🔹 Probando {sort_func}")
    sorted_list = getattr(sll, sort_func)(lista_copia, default_sort_criteria)
    sll.print_list(sorted_list)
