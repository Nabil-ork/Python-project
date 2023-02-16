les_routes=[]
def creeroute():
    if len(les_routes) <99:
        r=[input("entre le nom de la route: "), float(input("entre la longueur de la route en Km: ")), input("entre la ville de depart: "), input("entre la ville d'arrivée: ")]
        les_routes.append(r)
    else:
        print("le nombre des routes enregistre atteinte le maximum ")
def  affichage():
    for i in range(len(les_routes)):
        print("la route numero ", i+1,": ","\nLe nom: ", les_routes[i][0], "\nLa longueur: ", les_routes[i][1], " Km", "\nLa ville de départ: ", les_routes[i][2], "\nLa ville d'arrivée: ", les_routes[i][3])
def chercher():
    rp=int(input("comment vou voulez cherchez ?\n1 Par Nom\n2 Par longueur\n3 Par ville de depart\n4 Par ville d'arrivée\n----> "))
    if rp==1:
        cherche=input("entre le nom du route")
        for i in range(len(les_routes)):
            if cherche==les_routes[i][0]:
                print("c'est la route numero", i+1)
                a=i
            else:
                print("la route est introuvable")
    elif rp==2:
        cherche = int(input("entre la longueur du route"))
        for i in range(len(les_routes)):
            if cherche==les_routes[i][1]:
                print("c'est la route numero", i + 1)
                a=i
            else:
                print("la route est introuvable")
    elif rp==3:
        cherche = int(input("entre le ville de depart: "))
        for i in range(len(les_routes)):
            if cherche==les_routes[i][2]:
                print("c'est la route numero", i + 1)
                a=i
            else:
                print("la route est introuvable")
    elif rp==4:
        cherche = int(input("entre le ville de depart: "))
        for i in range(len(les_routes)):
            if cherche==les_routes[i][3]:
                print("c'est la route numero", i + 1)
                a=i
            else:
                print("la route est introuvable")
def supprimer(a):
    chercher()
    les_routes.pop(a)
def sauvgarder():
    f = open("route.txt", "w")
    for i in range(len(les_routes)):
        f.write(les_routes[i][0] + " " + les_routes[i][1] + " " + les_routes[i][2] + les_routes[i][3] + " " +"\n")
    f.close()

quite= True
while quite:
    print("Choisir une operation : ")
    print("1 pour ajouter une nouvelle route : ")
    print("2 pour afficher toutes les routes: ")
    print("3 pour chercher une route : ")
    print("4 pour supprimer une route : ")
    print("5 pour sauvegarder dans un fichier : ")
    print("0 pour sortir :")
    num=True
    while num:
        num= False
        sortir= int(input("------>"))

        if sortir==1:
            creeroute()
        elif sortir==2:
            affichage()
        elif sortir==3:
            chercher()
        elif sortir==4:
            supprimer()
        elif sortir==5:
            sauvgarder()
        elif  sortir==0:
            quite=False
        elif sortir>5 and sortir<0 :
            num=False
            print("entre un autre nombre: ")


