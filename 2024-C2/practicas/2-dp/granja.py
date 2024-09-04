import numpy as np

def resolver_granja(x, y, accumulated_arvejas, cache):
    """Devuelve la mayor cantidad de arvejas que se puede obtener empezando por la posicion (x, y) y con ese numero de arvejas acumuladas."""
    accumulated_arvejas = accumulated_arvejas + matriz_granja[x][y - 1]

    if y < largo - 1:
        return suma

    if suma % (cant_arvejas_modulo + 1) == 0:
        return suma
    else:
        return -1



def solve(ancho, largo, cant_arvejas_modulo, matriz_granja):
    cache = np.full((largo, ancho), -1, dtype=np.int64)
    return np.max()
