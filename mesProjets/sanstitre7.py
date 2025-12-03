# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:49:45 2025

@author: Chaïma Assoumani
"""
poids_perdu1 = float(input("Utilisateur 1 - Entrez le poids perdu (en kg) : "))
poids_perdu2 = float(input("Utilisateur 2 - Entrez le poids perdu (en kg) : "))

# Comparer les valeurs et afficher le résultat
if poids_perdu1 > poids_perdu2:
    print("Utilisateur 1 a perdu le plus de poids :", poids_perdu1, "kg")
elif poids_perdu2 > poids_perdu1:
    print("Utilisateur 2 a perdu le plus de poids :", poids_perdu2, "kg")
else:
    print("Égalité dans la perte de poids.")
