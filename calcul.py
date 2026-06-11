def ajouter(a, b):
    return a + b  # <-- Vérifie bien qu'il y a un "+" ici !

def soustraire(a, b):
    return a - b  # <-- Et un "-" ici !
def diviser(a, b):
    if b == 0:
        return "Erreur : Division par zéro"
    return a / b