import random, string

#fonction pour permettre a l'utulisateur de choisir un niveau
def choix_niveau():
    choix = 0
    while (choix != 1 and choix != 2 and choix != 3):
        print("Choisir un niveau de 1 a 3: ")
        choix = int(input("Entrer un nombre"))
        print("####################################")
    return choix



#fonction affichage du pendu en fonction du nombre de tentatives
def pendu(tentatives):
    if tentatives == 6:
        print(" ====y=========")
        print(" ||/ | ")
        print(" ||    ")
        print(" ||    ")
        print(" ||    ")
        print("/||    ")
        print("==============\n")
    if (tentatives == 5):
        print("=====Y========")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" ||  ")
        print("/|| ")
        print("==============\n")
    if (tentatives == 4):
        print("=====Y======== ")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" || /")
        print("/|| ")
        print("==============\n")
    if (tentatives == 3):
        print("=====Y========")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" || /|")
        print("/|| ")
        print("==============\n")
    if (tentatives == 2):
        print(" ====Y=========")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" || /|\ ")
        print("/|| ")
        print("==============\n")
    if (tentatives == 1):
        print(" ====Y========= ")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" || /|\ ")
        print("/|| / ")
        print("==============\n")
    if (tentatives < 0):
        print("=====Y======== ")
        print(" ||/ | ")
        print(" ||  0 ")
        print(" || /|\ ")
        print("/|| / \ |")
        print("==============\n")

#fonction permets de charger un mot dans la liste en fonction du niveau
def charger_mots():
    niveau = choix_niveau()

    # mots=[]
    motsFile = open('mots.txt')
    mots = list(motsFile.read().split('\n'))
    mot = ""
    print("Vous avez choisi le niveau ", niveau)
    print("chargement des donnéés...")
    print("8964 mots chargés")
    if (niveau == 1):
        while (not (2 <= len(mot) <= 4)):
            mot = random.choice(mots)
    if (niveau == 2):
        while (not (5 <= len(mot) <= 7)):
            mot = random.choice(mots)
    if (niveau == 3):
        while (not (len(mot) > 7)):
            mot = random.choice(mots)
    # chaine=mot.replace("\\n","");
    # chaine=mot.replace(" ","")
    # chaine="fatima"
    print(mot)
    print("je vous propose un mot de ", len(mot), " lettres.De quel mot s'agit-t'il?")
    print("#################################################")
    return mot

#fonction pour afficher le mot dans le jeu
def affichage_mot(lettres_trouvees,solution):
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "-"
    return affichage

#fontion pour jouer une partie
def jeu(solution,num_partie):
    tab_score=[]
    score=0
    score_max=0
    nb_tent_rest=0
    nb_lettre_unique=0
    point_erreur = 3
    lettres_trouvees = ""
    tentatives = 6
    affichage = ""
    voyelles = ["a", "e", "i", "o", "u", "y"]

    for l in solution:
        affichage += "-"
    while (tentatives > 0):
        print(affichage)
        proposition = input("saisir une lettre: ")
        if proposition in solution and proposition not in lettres_trouvees:
            lettres_trouvees += proposition
            print("Bravo, lettre correcte")
        else:
            if not proposition.isalpha():
                point_erreur -= 1
                print("Vous ne devez saisir que des lettres de l'alphabet \n il vous reste", point_erreur,
                      "avertissements")

            else:
                if proposition in lettres_trouvees:
                    point_erreur -= 1
                    print("lettre deja trouve\nil vous reste",point_erreur,"avertissement")
                else:
                    if proposition in voyelles:
                        print("Vous avez saisi une voyelle qui n'est pas dans le mot.\nVous perdez deux tentatives. ")
                        print("#########################################")
                        tentatives -= 2
                    else:
                        print("Vous avez saisi une consonne qui n'est pas dans le mot.\nVous perdez une tentative.")
                        tentatives -= 1
            if (point_erreur == 0):
                print("vous avez epuisez votre cartouche de points erreurs")
                tentatives -= 1
            if(tentatives>0):
                print("il vous reste", tentatives, "tentatives")
                print("######################################")
            pendu(tentatives)
            print("______________________________________________________")

        affichage=affichage_mot(lettres_trouvees, solution)
        if "-" not in affichage:
            nb_lettre_unique = nombre_lettre_unique(solution)
            score = tentatives * nb_lettre_unique
            print("SC",score)
            print("______________________________________________________")
            print("Félicitation : Vous avez deviné le mot.")
            print("Votre score:",score)
            if score>score_max:
                score_max=score
                print("vous avez battu votre score ,votre score maximal est de:",score_max)
            break
    if (tentatives <= 0):
        print("Vous avez perdu :(")
        print("le mot ete:",solution)

    log_name(num_partie,1,score,tentatives)

#fonction pour calculer le nombre de lettre unique
def nombre_lettre_unique(solution):
    nb_lettre_unique=0
    d1=dict()
    for c in solution:
        if c in d1:
            d1[c]=d1[c]+1
        else:
            d1[c] = 1
    for c in solution:
        if d1[c]==1:
           nb_lettre_unique+=1
    return nb_lettre_unique

#fonction pour ecrire dans le log_name.txt
def log_name(niveau,score,nb_tentatives,num_partie):
    fichier=open("log_name.txt","w")
    fichier.write("partie:"+str(num_partie)+"\nniveau:"+str(niveau)+"\nle score"+str(score)+"\nnombre de tentatives"+str(nb_tentatives))
    fichier.close()


if __name__ == '__main__':
    nombre_lettre_unique()
