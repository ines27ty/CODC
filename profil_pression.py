from math import *
import numpy as np
import matplotlib.pyplot as plt
import os

# Paramètres
d= 0.1
L = 1
H = 0.6
g = 9.81
mu = 1.78e-5
rho = 1.2

# Paramètres à changer
Q = 10
K = 1e-7

directory = os.getcwd # Remplace par le chemin correct

# Calcul de la vitesse à la section du milieu poreux
u_Darcy = Q/(L*1*3600)
print("Vitesse Darcy",u_Darcy)

# Calcul de la pression à partir de la vitesse et la loi de Darcy
P_th =u_Darcy*mu/K
print("Delta P théorique",P_th)


# Lire les lignes du fichier
with open('pressure_u_0.35_k_107.xy', 'r') as fichier:
    lines = fichier.readlines()

# Initialiser des listes pour les positions et pressions
position = []
pression = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split(',')  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position.append(float(values[0]))
    pression.append(float(values[1]))

# Calculer la moyenne de la pression
mean_pression = np.mean(pression)

# Calcul de l'écart relatif pour la pression
ec_pression = [(pression[i] - mean_pression) * 100 / mean_pression for i in range(len(pression))]


# Afficher le graphique pour la pression de ce fichier et la pression moyenne et la pression théorique
plt.figure() 
plt.plot(position, pression, label="Simulation")
plt.axhline(mean_pression, color='r', label="Moyenne de la simulation = {:.2e}".format(mean_pression))
#plt.axhline(P_th, color='g', label="Théorique = {:.2e}".format(P_th))
plt.xlabel("Position (m)")
plt.ylabel("Pression (Pa)")
plt.grid()
plt.legend()
plt.title(f"Pression")
plt.savefig(f"pressure_u_0.35_k_107.png")  # Sauvegarder le graphique