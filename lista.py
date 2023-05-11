"""
    En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, 
    se solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es:
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
"""
#Variable dada
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
#Se crea variable vacia
mi_lista_2 = []
mi_lista_2 = mi_lista [0:1]
#Se usa for range para recorrer lista
for n in range(len(mi_lista)):
    if mi_lista[n] not in mi_lista_2:
        #Se agrega los números a mi_lista_2
        mi_lista_2.append(mi_lista[n])
#Se llama la función print para mostrar en pantalla la lista sin números repetidos
print(mi_lista_2)
#Se usa el método sort para ordenar los números
mi_lista_2.sort()
#Se llama la función print para mostrar en patalla la lista de menor a mayor
print(mi_lista_2)