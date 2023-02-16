class avion:
    def __init__(self,numero,nom,capacite,cout_par_place) :
        self.__numero = numero
        self.__nom = nom
        self.__capacite = capacite
        self.__cout_par_place = cout_par_place
        self.__pilote = None
    def get__numero(self) :
        return self.__numero
    def set__numero(self, numero) :
        self.__numero=numero
    def get__nom(self):
        return self.__nom
    def set__nom(self, nom):
        self.__nom=nom
    def get__capacite(self):
        return self.__capacite
    def set__capacite(self, capacite):
        self.__capacite=capacite
    def get__cout_par_place(self):
        return self.__cout_par_place
    def set__cout_par_place(self, cout_par_place):
        self.__cout_par_place=cout_par_place
    def get__pilote(self):
        return self.__pilote
    def aff_pilote(self, pilote):
        self.__pilote=pilote
    def augmentation_salaire(self):
        self.__pilote.set__salaire(p1.get__salaire()+self.couttotal()*0.1)
    def affichage (self) :
        print("numero :", self.__numero, "\nNom :", self.__nom, "\ncapacite :", self.__capacite, "\nLe cout par place :",
                  self.__cout_par_place,"\n le nom du pilot :", p1.get__nom(),"\n le prenom du pilot :", p1.get__prenom(),"\n le salaire du pilot :", p1.get__salaire())
    def couttotal(self):
        return self.__cout_par_place * self.__capacite

class pilote:
    def __init__(self):
        self.__nom=""
        self.__prenom=""
        self.__salaire = 0
    def get__nom(self):
        return self.__nom
    def set__nom(self, nom):
        self.__nom=nom
    def get__prenom(self):
        return self.__prenom
    def set__prenom(self, prenom):
        self.__prenom=prenom
    def get__salaire(self):
        return self.__salaire
    def set__salaire(self, salaire):
        self.__salaire = salaire
    def salaireannuel(self):
        return self.__salaire*12

