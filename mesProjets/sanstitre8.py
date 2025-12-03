# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:51:02 2025

@author: Chaïma Assoumani
"""
poids_initial1 = float(input("Utilisateur 1 - Entrez votre poids initial (en kg) : "))
poids_initial2 = float(input("Utilisateur 2 - Entrez votre poids initial (en kg) : "))

# Initialiser la perte totale pour chaque utilisateur
perte_totale1 = 0
perte_totale2 = 0

# Simuler 5 semaines de régime
for semaine in range(1, 6):
    print(f"\nSemaine {semaine} :")
    
    perte1 = float(input("Utilisateur 1 - Poids perdu cette semaine (en kg) : "))
    perte2 = float(input("Utilisateur 2 - Poids perdu cette semaine (en kg) : "))
    
    perte_totale1 += perte1
    perte_totale2 += perte2

# Afficher le résultat final
    print(f"Utilisateur 1 a perdu le plus de poids : {perte_totale1} kg")
elif perte_totale2 > perte_totale1:
    print(f"Utilisateur 2 a perdu le plus de poids : {perte_totale2} kg")
print("\nRésultat final après 5 semaines :")

if perte_totale1 > perte_totale2:
else:
    print(f"Égalité parfaite ! Les deux ont perdu {perte_totale1} kg")
