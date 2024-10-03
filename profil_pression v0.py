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
Q = [1,10,10]*3
K = 1e-8

directory = os.getcwd # Remplace par le chemin correct

# Calcul de la vitesse à la section du milieu poreux
u_Darcy = Q/(L*1*3600)
print("Vitesse Darcy",u_Darcy)

# Calcul de la pression à partir de la vitesse et la loi de Darcy
P_th =u_Darcy*mu/K
print("Delta P théorique",P_th)



# Dictionnaire pour stocker les écarts relatifs de chaque fichier
ec_pression_dict = {}  # Stockage des écarts relatifs par fichier

# Parcourir tous les fichiers du répertoire courant
for filename in os.listdir('.'):  # Parcourir tous les fichiers dans le répertoire actuel
    if filename.endswith(".xy") and filename.startswith("pression"):
        # Lire les lignes du fichier
        with open(filename, 'r') as fichier:
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
        
        # Stocker cette liste d'écarts relatifs dans le dictionnaire avec le nom du fichier
        ec_pression_dict[os.path.splitext(filename)[0]] = ec_pression

        # Afficher le graphique pour la pression de ce fichier et la pression moyenne et la pression théorique
        plt.figure() 
        plt.plot(position, pression, label="Pression (Pa)")
        plt.axhline(mean_pression, color='r', label="Pression moyenne")
        plt.axhline(P_th, color='g', label="Pression théorique")
        plt.xlabel("Position (m)")
        plt.ylabel("Pression (Pa)")
        plt.grid()
        plt.legend()
        plt.title(f"Pression- {filename}")
        plt.savefig(f"pression{os.path.splitext(filename)[0]}.png")  # Sauvegarder le graphique