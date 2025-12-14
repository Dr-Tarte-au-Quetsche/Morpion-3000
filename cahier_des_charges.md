Stats morpion Python :
	Utilisation dico stats 
	Fichier global de stats (nom : « main.json/txt »)
		En tête : « Statistiques du Morpion : »
		-Le nombre de parties au total
		- Combine les autres fichiers de parties en faisant un read
	Création fichiers automatiquement à chaque fin de partie (json ou txt) des parties en donnant les pseudo des joueurs (nom : « PseudoJ1_vs_PseudoJ2.json/txt » 
	Prévoir le cas où il y a le même pseudo pour le joueur 1 et 2 et donc le même nom de fichier
		En tête : « PseudoJ1 contre PseudoJ2 : »
	
		-Le nombre de parties gagnées J1
		- Le nombre de manches gagnées  J1
		-Le pourcentage des victoires J1(en fonction du nombre de parties gagnées)
		-Le nombre de parties gagnées J2
		-Le pourcentage de victoires J2


Partie : 
Empêcher un joueur d’écraser une position déjà occupée
Effacer les positions disponibles dans la grille_numpad

Calcul score d’une partie:
à chaque manche gagné score du joueur gagnant +=1
fin de partie affiche le joueur qui a le plus gros score
