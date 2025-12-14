def test(grille_jeu,debut,fin,pas) :
    total = 0
    for idx_case in range(debut,fin,pas) :
        total += grille_jeu[idx_case]
        if total == 3 :
            return 1
        elif total == -3 :
            return -1



def test2(grille_jeu) :
    debut = 0
    fin = 9
    pas = 1
    while debut < 7 :
        test(grille_jeu, debut, fin, pas)
        debut +=3

    debut = 0
    fin = 9
    pas = 3
    while debut < 4 :
        test(grille_jeu, debut, fin, pas)
        debut +=1





grille_morpion = [0,0,-1,
                1,1,1,
                0,0,0]

print(test2(grille_morpion))
