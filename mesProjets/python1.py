# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:22:21 2025

@author: Chaïma Assoumani
""
# 1 je declare les variables et afficher leurs types 
nom = "KAINA"
age = 23
taille = 1.68
estEtudiant = True

print(type(nom))
print(type(age))
print(type(taille))
print(type(estEtudiant))
"""
"""
# 2 les opérations
# 3 Affichage en python , il exixte 4 façon d'affichage 
nom = "Imane"
age = 23 
#premier affichge
print("Bonjour, je m'appeelle", nom, "et j'ai",age,"ans")
#2e aff
print("Bonjour, je m'appelle "   + nom +  " et j'ai " +  str(age) +" ans")
#3e aff
print(f"Bonjour, je m'appelle {nom} et j'ai {age} ans")
#4e aff
print("Bonjour, je m'appelle {} et j'ai {} ans ".format(nom, age))
"""
 #Entrée de l'utilisateur
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre age :")) #conversion en entier 
print(f"Bonjour {nom}, vous avez {age} ans ")

 
 