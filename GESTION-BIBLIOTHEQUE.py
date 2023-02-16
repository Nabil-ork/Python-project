from livre import Livre
import os
class etagere:
    nblvr = 0
    def __init__(self,listlvr):
        self.__nbLivre=etagere.nblvr
        self.__listlvr=listlvr
    def infoetagere(self):
        return "Le nombre de livres que pourra contenir l'étagère est "+ str(self.__nbLivre) +".\nLe nombre de livres dans l'etagére est: " + len(self.__listlvr)
    def ajoute(self,livre):
        if len(self.__listLivres) < self.__nbLivre:
            self.__listLivres.append(livre)
            print("Le livre a été ajouté avec succès.")
        else:
            print("L'étagère est pleine ")
    def recupere(self,i):
        if i >= 1 and i <= len(self.__listLivres)+1:
            return self.__listLivres[i - 1]
        else:
            return "Ce livre n'exist pas. "
    def chercher(self,titre,auteur):
        ex = False
        for livre in self.__listlvr:
            if livre.get_Auteur() == auteur and livre.get_Titre() == titre:
                ex = True
                c = self.__listlvr.index(livre) + 1
                break
            else:
                c = 0
            return c
    def Chercher(self,titre,auteur):
        ex = False
        lesPositions = []
        for livre in self.__listlvr:
            if livre.get_Auteur() == auteur and livre.get_Titre() == titre:
                ex = True
                lesPositions.append(self.__listlvr.index(livre) + 1)
        return lesPositions
        if not ex:
                return 0
    def memeAuteur(self,auteur):
        ex = False
        livresAuteur = []
        for livre in self.__listlvr:
            if livre.get_Auteur() == auteur:
                ex = True
                livresAuteur.append(livre)
        if not ex:
            return None
        else:
             return livresAuteur

    def memeTitre(self,titre):
        ex = False
        livresTitre = []
        for livre in self.__listlvr:
            if livre.get_Titre() == titre:
                ex = True
                livresTitre.append(livre)
        if not ex:
                return None
        else:
            return livresTitre

    def enlever(self,i):
        ex =False
        if i >= 1 and i <= len(self.__listlvr):
            for i in range(i-1,((len(self.__listlvr))-1)):
                self.__listlvr[i] = self.__listlvr[i+1]
            del self.__listlvr[-1]
        else:
            return None

    def EnleverLivre(self,titre,auteur):
        ex = False
        T=[]
        for livre in self.__listlvr:
            if livre.get_Auteur() == auteur and livre.get_Titre() == titre:
                ex = True
                T.append(livre)
        for i in T:
            self.__listlvr.remove(i)
        if not ex :
            return None


#--------------------------------------------------------------------------
def menu():
    print("-".rjust(63,"-"))
    print("Menu:".rjust(33))
    print("-".rjust(63,"-"))
    print("1 pour affichier les information sur L'etagere :")
    print("2 pour affichier les information sur L'etagere et les livres qui contient :")
    print("3 pour affichier un livre selon sur ça position :")
    print("4 pour ajouter un livre dans une etagere :")
    print("5 pour affichier la position d'un livre selon le auteur et le titre :")
    print("6 pour affichier la position de tous les livres avec le meme auteur et le meme titre :")
    print("7 pour affichier les livres rediger par le meme auteur :")
    print("8 pour affichier les livres avec le meme titre :")
    print("9 pour supprimer un livre par ça position : ")
    print("10 pour supprimer un livre par auteur et titre : ")
    print("11 pour supprimer tout les livres avec le meme titre et auteur :")
    print("12 pour vider l'ecran :")
    print("13 pour sortir :")
    print("-".rjust(63,"-"))
# L1 = Livre("LIVRE1","A",285,70)
# L2 = Livre("LIVRE2","Z",562,88)
# L3 = Livre("LIVRE3","E",654,120)
# L4 = Livre("LIVRE4","R",765,150)
# L5 = Livre("LIVRE5","T",953,180)
# L6 = Livre("LIVRE6","Y",553,2500)
# L7 = Livre("LIVRE7","U",105,235)
# L8 = Livre("LIVRE8","I",536,175)
# L9 = Livre("LIVRE9","O",453,250)
# L10 = Livre("LIVRE10","P",352,215)
# L11 = Livre("LIVRE11","Q",516,220)
# L12= Livre("LIVRE12","S",275,100)
# L13 = Livre("LIVRE13","D",451,220)

# E1 = Etagere(5,[L1,L2,L3,L4])
# E2 = Etagere(7,[L13,L7,L8,L9,L10,L11,L12])

while True:
    menu()
    choix = input("Entrer votre choix : ")
    print("-".rjust(63,"-"))

    if choix == "13":
        print("A la prochaine fois .")
        break

    if choix == "1":
        print(E1.info())

    if choix == "2":
        print(E1)

    if choix == "3":
        print(E1.getLivre(2))

    if choix == "4":
        try:
            E1.ajouter(L13)
        except EtagerePleineException as e:
            print(e)
#--------------------------------------------------------------------------
    if choix == "5":
        if E1.chercher("Les Misérables","Victor Hugo") != 0 :
            print("La position de livre a la recherche est",E1.chercher("Les Misérables","Victor Hugo"),".")
        else:
            print("Ce livre n'existe pas !")
#--------------------------------------------------------------------------
    if choix == "6":
        if len(E1.Chercher("Les Misérables","Victor Hugo")) != 0 :
            print("Les position des livres a la recherche sont",E1.Chercher("Les Misérables","Victor Hugo"),".")
        else:
            print("Ce livre n'existe pas !")

    if choix == "7":
        if len(E1.meme_auteur("George R.R Martin")) != 0:
            for livre in E1.meme_auteur("George R.R Martin"):
                print(livre)
        else:
            print("Il n'y a pas des livres de cet auteur :")

    if choix == "8":
        if len(E1.meme_titre("Les Misérables")) != 0:
            for livre in E1.meme_titre("Les Misérables"):
                print(livre)
        else:
            print("Il n'y a pas des livres de cet titre :")
#
    if choix == "9":
        if E2.enleverLivre(5) != None:
            print("Terminer !")
        else:
            print("La position n'existe pas ! ")
#
    if choix == "10":
        if E1.EnleverLivre("A Game of Thrones","George R.R Martin") != None:
            print("Terminer !")
        else:
            print("Ce livre n'existe pas ! ")

    if choix == "11":
        l = E2.enlever("The Return Of The King","J.R.R Tolkien")
        if l != 0:
            print("Les livres qui sont supprimer :")
            for livre in l:
                print(livre)
        else:
            print("Ce livre n'existe pas ! ")

    if choix == "12":
        os.system("clear")
