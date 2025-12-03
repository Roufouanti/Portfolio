# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:48:54 2025

@author: Chaïma Assoumani
"""
score1 = float(input("Entrez le premier score : "))
score2 = float(input("Entrez le deuxième score : "))

# Comparer les scores et afficher le résultat
if score1 > score2:
    print("Le gagnant est le premier score :", score1)
elif score2 > score1:
    print("Le gagnant est le deuxième score :", score2)
else:
    print("Égalité")
