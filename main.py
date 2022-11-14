from bibliotheque import *
if __name__ == '__main__':

        continuer=0
        num_partie = 1
        print("PARTIE 1")
        print("\nBienvenue dans le jeu LET-GET")
        print("###########################################")
        while(continuer==0):
               print("vous avez 3 points erreurs")
               print("###########################################")
               print("Vous avez 6 tentatives")
               print("###########################################\n\n")
               pendu(6)
               jeu(charger_mots(),num_partie)
               print("---------------------------------------------------------------------------------------------------------------------")
               num_partie += 1
               print("PARTIE", num_partie)
               continuer=int(input("VOULEZ VOUS CONTINUER? \n TAPPEZ 0 POUR CONTINUER ET UN AUTRE CHIFFRE POUR QUITTER:"))

        print("**************************************************************************************************************************************")
        print("CIAO")
        print("A LA PROCHAINE :)")
        print("**************************************************************************************************************************************")

