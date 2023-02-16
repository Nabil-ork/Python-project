def playing():
    play_game = input('do you want to play again ? y= yes, no \n')
    if play_game =='yes':
        pl=True
    elif play_game =='no':
        pl=False
        print('thanks for playing')
    return pl
def dmain(domaine):
    import random
    rp=int(input("----->"))
    if rp==1:
        x="couleurs"
    elif rp == 2:
        x ="sport"
    elif rp == 3:
        x ="payes"
    mot=random.choice(domaine)
    print(mot)
    return mot
def letter(mot):
    tmot=[mot]
    print(tmot)
    for letter in mot:
        tmot.append(letter)

domaine = {"couleurs":'rouge,vert,bleu,jaune,violet,noir,orange,rose,maron,gris,blan',"sport":'football,basketball,rugby,tennis,golf,hockey,',"payes":"maroc,algerie,france,usa,emarat,israël "}
#print("choisissez le domaine que vous voulez :\n 1 couleurs \n 2 sport \n 3 payes")



rpletter="a"
c=0
img=["   _____ \n  |      \n  |      \n  |      \n  |      \n  |      \n  |      \n__|__\n",
     "   _____ \n  |     | \n  |     |\n  |      \n  |      \n  |      \n  |      \n__|__\n",
     "   _____ \n  |     | \n  |     |\n  |     | \n  |      \n  |      \n  |      \n__|__\n",
     "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |      \n  |      \n__|__\n",
     "   _____ \n  |     | \n  |     |\n  |     | \n  |     O \n  |    /|\ \n  |    / \ \n__|__\n"]
for i in range(len(tmot)):
    while tmot[i]!=rpletter:
        c+=1
        print(img[c-1])
        print("votre reponse est faux")
        for i in range(len(tmot)):
            if rpletter==tmot[i]:
                print("la letter est placé dans la place", str(i+1))
        if c==5:
            print("vous n'arrivez pas a devine le mot")
            break





