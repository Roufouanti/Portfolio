# -*- coding: utf-8 -*-
"""
Created on Tue May  6 16:32:00 2025

@author: Chaïma Assoumani
"""

# Création d'une liste de 5 entiers
L = [12, 7, 9, 14, 20]

# 1) Afficher la valeur de L[3]
print("1) La valeur de L[3] est :", L[3])

# 2) Modifier la liste
L[2] = 5  # Remplacer L[2] par 5
L[3] = L[2] + L[4]  # Remplacer L[3] par la somme de L[2] et L[4]

# Afficher la liste modifiée
print("2) La liste après modification :", L)