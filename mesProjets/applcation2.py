# -*- coding: utf-8 -*-
"""
Created on Tue May  6 16:37:28 2025

@author: Chaïma Assoumani
"""

# Définir la liste
liste = [17, 38, 10, 25, 72]

# Trier et afficher la liste
liste.sort()
print("Liste triée :", liste)

# Ajouter l'élément 12 à la liste et afficher la liste
liste.append(12)
print("Après ajout de 12 :", liste)

# Renverser et afficher la liste
liste.reverse()
print("Liste renversée :", liste)

# Afficher l'indice de l'élément 17
indice_17 = liste.index(17)
print("Indice de l'élément 17 :", indice_17)

# Enlever l'élément 38 et afficher la liste
liste.remove(38)
print("Après suppression de 38 :", liste)