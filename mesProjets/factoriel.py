# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:05:08 2025

@author: Chaïma Assoumani
"""

import math

#  on demande un nombre à l'utilisateur
n = int(input("Entrez un n entier positif : "))

# on calcule le factoriel en utilisant la fonction math.factorial
resultat = math.factorial(n)

# Afficher le résultat
print(f"Le factoriel de {n} est {resultat}")