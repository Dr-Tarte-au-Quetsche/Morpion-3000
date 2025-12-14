import random
import os

gagnant = False
tuple_signes = ("❌","🔵")
dicoj1 = {"id" : 1, "pseudo" : "J1", "signe" : "❌", "prio" : 1, "toggle" : 1}
dicoj2 = {"id" : -1, "pseudo" : "J2", "signe" : "🔵", "prio" : 2, "toggle" : 0} 
####################################################################################"
# Partie Matrice
grille_numpad = [7,8,9,
                4,5,6,
                1,2,3]

grille_morpion = [0,0,0,
                0,0,0,
                0,0,0]

dico_numpad = {7 :0, 8: 1, 9 : 2,
                4 : 3, 5 : 4, 6 : 5,
                1 : 6, 2 : 7, 3 :8}

#Partie modif de pseudo
##########################################################################################################################

def modif_pseudo_j2 (pseudo) :
    dicoj2["pseudo"] = pseudo
    print(f"Votre pseudo a bien été enregistré : Bienvenue {dicoj2['pseudo']} ! \n")

def modif_pseudo_j1(pseudo) :
    dicoj1["pseudo"] = pseudo
    print(f"Votre pseudo a bien été enregistré : Bienvenue {dicoj1['pseudo']} ! \n")
##########################################################################################################################
#Définition de la fonction qui choisira quel joueur commencera
##########################################################################################################################
def affichage_prio () :
    joueur_random = random.randint(1,2)
    if joueur_random == 1 :
        dicoj1["prio"] = 1
        dicoj1['toggle'] = 1

        dicoj2["prio"] = 2
        dicoj2["toggle"] = 0
        print(f'C\'est {dicoj1["pseudo"]} qui commence ! \n')
        return 1
    
    else :
        dicoj2["prio"] = 1
        dicoj2["toggle"] = 1

        dicoj1["prio"] = 2
        dicoj1["toggle"] = 0
        print(f'C\'est {dicoj2["pseudo"]} qui commence ! \n ')
        return -1
##########################################################################################################################

#Fonction d'affectation du signe en fonction du joueur prioritaire
def affectation_signe_joueur(signe_joueur) :
    

    if dicoj1["prio"] == 1 :

        if signe_joueur.upper() == 'X' :
            dicoj1["signe"] = tuple_signes[0]
            dicoj2["signe"] = tuple_signes[1]
            print(f"{dicoj1['pseudo']} obtient le signe ❌ ! \n")
            print(f"{dicoj2['pseudo']} obtient donc le signe 🔵 ! \n")
        else :
            dicoj1["signe"] = tuple_signes[1]
            dicoj2["signe"] = tuple_signes[0]
            print(f"{dicoj1['pseudo']} obtient le signe 🔵 ! \n")
            print(f"{dicoj2['pseudo']} obtient donc le signe ❌ ! \n")
    else :
        if signe_joueur.upper() == 'X' :
            dicoj2["signe"] = tuple_signes[0]
            dicoj1["signe"] = tuple_signes[1]
            print(f"{dicoj2['pseudo']} obtient le signe ❌ ! \n" )
            print(f"{dicoj1['pseudo']} obtient donc le signe 🔵 ! \n")
        else :
            dicoj2["signe"] = tuple_signes[1]
            dicoj1["signe"] = tuple_signes[0]
            print(f"{dicoj2['pseudo']} obtient le signe 🔵 ! \n")
            print(f"{dicoj1['pseudo']} obtient donc le signe ❌ ! \n ")

##########################################################################################################################


##########################################################################################################################



#Partie grille morpion :
def modif_grille(id_signe_joueur,position) :
    grille_morpion[dico_numpad[position]] = id_signe_joueur

def remplir_grille(grille) :
    grille_graphique = [0,0,0,0,0,0,0,0,0]
    for idx_signe in range(len(grille)) :
        if grille[idx_signe] == 0 :
            grille_graphique[idx_signe] = "⬜"
        elif grille[idx_signe] > 0 :
            grille_graphique[idx_signe] = dicoj1["signe"]
        else :
            grille_graphique[idx_signe] = dicoj2["signe"]
    return grille_graphique


def affiche_grille_morpion(titre, tableau) :
    tabgrille = remplir_grille(tableau)
    grille= f"{titre}\n----------------\n"       #Affichage du menu
    compteur = 0
    for element in tabgrille:
        compteur += 1
        grille+= "| "+str(element) + " "
        if compteur > 2 :
            grille += "|\n----------------\n"
            compteur = 0
    return grille

def affiche_grille_numpad(titre,tableau) :
    grille= f"{titre}\n-------------\n"       #Affichage du menu
    compteur = 0
    for element in tableau:
            compteur += 1
            grille+= "| "+str(element) + " "
            if compteur > 2 :
                grille += "|\n-------------\n"
                compteur = 0
    return grille

###############################################################################
#Fonctions pour la partie de jeu
#Test de victoires##########################################################################################""
def test_victoire(grille_jeu) :
    #Test lignes horizontales
    total = 0
    debut = 0
    fin = 3
    pas = 1
    for idx_case in range(debut,fin,pas) :
        total += grille_jeu[idx_case]
        if total == 3 :
            return 1
        elif total == -3 :
            return -1
        if fin < 9 :
            fin += 2

#Test lignes verticales
    total = 0
    debut = 0
    fin = 9
    pas = 3
    for idx_case in range(debut,fin,pas) :
        total += grille_jeu[idx_case]
        if total == 3 :
            return 1
        elif total == -3 :
            return -1
        elif debut < 3 :
            debut += 1
    #Test diagonales

    addition_diago1 = 0
    addition_diago1 = addition_diago1 + grille_morpion[0] + grille_morpion[4] + grille_morpion[8]
    if addition_diago1 == 3 :
        return 1
    elif addition_diago1 == - 3 :
        return -1

    addition_diago2 = 0
    addition_diago2 = addition_diago2 + grille_morpion[2] + grille_morpion[4] + grille_morpion[6]
    if addition_diago2 == 3 :
        return 1
    elif addition_diago2 == - 3 :
        return -1
############################################################################################
def manche(nombre_manche) :
    while 0 in grille_morpion == True :
        while test_victoire() == False :
            pass

def partie() :
    manche()
###############################################################################
def statistiques() :
    pass



##################################################################################################################
# Test déroulement d'une partie

choixmodif_j1 = input(f"Monsieur/Madame Joueur·euse 1, Voulez-vous entrer votre pseudo ? (o/n) ---->")
if choixmodif_j1.lower() == "o" :
    pseudo_j1 = input("Entrez votre pseudo ----> ")
    modif_pseudo_j1(pseudo_j1)

choixmodif_j2 = input(f"Et vous Monsieur/Madame Joueur·euse 2, Voulez-vous entrer votre pseudo ? (o/n) ----> ")
if choixmodif_j2.lower() == "o" :
    pseudo_j2 = input("Entrez votre pseudo ----> ")
    modif_pseudo_j2(pseudo_j2)

affichage_prio()
if dicoj1["prio"] == 1 :
    choix_signe = input(f"Choisissez votre signe , {dicoj1['pseudo']} (X/O) ----> ")
else :
    choix_signe = input(f"Choisissez votre signe , {dicoj2['pseudo']} (X/O) ----> ")

affectation_signe_joueur(choix_signe)
##################################################################################################
while test_victoire(grille_morpion)[1] != 1 or test_victoire(grille_morpion)[1] != -1 :
    print(test_victoire(grille_morpion)[1])
    print(test_victoire(grille_morpion))
    if dicoj1["toggle"] == 1 :
        print(affiche_grille_numpad("Rappel grille :", grille_numpad))
        print(affiche_grille_morpion(f"Au tour de {dicoj1['pseudo']} : ", grille_morpion))

        position_user = int(input("Choissisez votre position -----> "))
        while grille_morpion[dico_numpad[position_user]] != 0 :
            position_user = int(input("La position est déjà prise ! Veuillez en choisir une autre ! ----> "))
        modif_grille(dicoj1["id"],position_user)
        grille_numpad[dico_numpad[position_user]] = "-"
        dicoj1["toggle"] = 1 - dicoj1["toggle"]
        dicoj2["toggle"] = 1 - dicoj2["toggle"]
    else :
        print(affiche_grille_numpad("Rappel grille :", grille_numpad))
        print(affiche_grille_morpion(f"Au tour de {dicoj2['pseudo']} : ", grille_morpion))
        position_user = int(input("Choissisez votre position -----> "))
        while grille_morpion[dico_numpad[position_user]] != 0 :
            position_user = int(input("La position est déjà prise ! Veuillez en choisir une autre ! ----> "))
        modif_grille(dicoj2["id"],position_user)
        grille_numpad[dico_numpad[position_user]] = "-"
        dicoj1["toggle"] = 1 - dicoj1["toggle"]
        dicoj2["toggle"] = 1 - dicoj2["toggle"]
else :
    print("zoiajnoifzanjoif")
