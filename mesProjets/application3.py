# -*- coding: utf-8 -*-
"""
Created on Tue May  6 16:37:33 2025

@author: Chaïma Assoumani
"""

# Initialiser T comme une liste vide
T = []

# Initialiser M comme une liste de 5 flottants nuls
M = [0.0, 0.0, 0.0, 0.0, 0.0]

# Afficher les listes T et M
print("Liste T :", T)
print("Liste M :", M)

# Utiliser range() pour afficher les entiers de 0 à 3
print("Entiers de 0 à 3 :", list(range(0, 4)))

# Utiliser range() pour afficher les entiers de 4 à 7
print("Entiers de 4 à 7 :", list(range(4, 8)))

# Utiliser range() pour afficher les entiers de 2 à 8 par pas de 2
print("Entiers de 2 à 8 par pas de 2 :", list(range(2, 9, 2)))

# Définir L comme une liste des entiers de 0 à 5
L = list(range(0, 6))
print("Liste L :", L)

# Tester l'appartenance des éléments 3 et 6 à L
print("3 appartient à L :", 3 in L)
print("6 appartient à L :", 6 in L)