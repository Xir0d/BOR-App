#Trad caractèresen liste

E=str(input("Veuillez entrer la suite de bits : "))
Entree=[]
for loop in range (len(E)):
    Entree=Entree+list(E[loop])

# préparation liste avec caractères traduits

resultat=[]
for loop_b in range (128):
    resultat.append("")

#Traduction 7 bits en un nombre

def trad_7 (aa,ab,ac,ad,ae,af,ag):
    if aa==0:
        n=0
    else:
        n=1
    if ab==1:
        n=n+2
    if ac==1:
        n=n+4
    if ad==1:
        n=n+8
    if ae==1:
        n=n+16
    if af==1:
        n=n+32
    if ag==1:
        n=n+64
    return(n)

#Traduction 6 bits en un nombre

def trad_6 (aa,ab,ac,ad,ae,af,):
    if aa==0:
        n=0
    else:
        n=1
    if ab==1:
        n=n+2
    if ac==1:
        n=n+4
    if ad==1:
        n=n+8
    if ae==1:
        n=n+16
    if af==1:
        n=n+32
    return(n)

#Traduction nombre en caractère

def dic (n):
    if n==0:
        return(" ")
    if n==1:
        return("u")
    if n==2:
        return("j")
    if n==3:
        return(",")
    if n==4:
        return(")")
    if n==5:
        return("t")
    if n==6:
        return("b")
    if n==7:
        return("ç")
    if n==8:
        return("m")
    if n==9:
        return("e")
    if n==10:
        return("-")
    if n==11:
        return("2")
    if n==12:
        return("r")
    if n==13:
        return("'")
    if n==14:
        return("9")
    if n==15:
        return("=")
    if n==16:
        return("3")
    if n==17:
        return("@")
    if n==18:
        return("s")
    if n==19:
        return("4")
    if n==20:
        return("/")
    if n==21:
        return("v")
    if n==22:
        return("!")
    if n==23:
        return("(")
    if n==24:
        return("i")
    if n==25:
        return("+")
    if n==26:
        return("è")
    if n==27:
        return("o")
    if n==28:
        return("à")
    if n==29:
        return(":")
    if n==30:
        return("é")
    if n==31:
        return("c")
    if n==32:
        return("l")
    if n==33:
        return("1")
    if n==34:
        return("<")
    if n==35:
        return("f")
    if n==36:
        return("g")
    if n==37:
        return("÷")
    if n==38:
        return("h")
    if n==39:
        return("0")
    if n==40:
        return("a")
    if n==41:
        return(";")
    if n==42:
        return("z")
    if n==43:
        return("²")
    if n==44:
        return('"')
    if n==45:
        return("y")
    if n==46:
        return("ù")
    if n==47:
        return("q")
    if n==48:
        return("5")
    if n==49:
        return("n")
    if n==50:
        return(".")
    if n==51:
        return("k")
    if n==52:
        return("x")
    if n==53:
        return("p")
    if n==54:
        return("8")
    if n==55:
        return("ß")
    if n==56:
        return("d")
    if n==57:
        return("7")
    if n==58:
        return("6")
    if n==59:
        return("w")
    if n==60:
        return("*")
    if n==61:
        return("?")
    if n==62:
        return("%")


#Récupération des indicatifs parmi le message et traduction en nombre

indicatif=[]
indicatif=trad_7(int(Entree[-7]),int(Entree[-6]),int(Entree[-5]),int(Entree[-4]),int(Entree[-3]),int(Entree[-2]),int(Entree[-1]))

secur1=0
secur1=trad_6(int(Entree[-19]),int(Entree[-18]),int(Entree[-17]),int(Entree[-16]),int(Entree[-15]),int(Entree[-14]))

secur2=0
secur2=trad_6(int(Entree[-13]),int(Entree[-12]),int(Entree[-11]),int(Entree[-10]),int(Entree[-9]),int(Entree[-8]))
secur2=(secur2*64)+secur1

#repérage des balises

Bls=[0]
for loop_d in range (len(Entree)):
    if int(Entree[loop_d])==1 :
        if int(Entree[loop_d+1])==1 :
            if int(Entree[loop_d+2])==1 :
                if int(Entree[loop_d+3])==1 :
                    if int(Entree[loop_d+4])==1 :
                        if int(Entree[loop_d+5])==1 :
                            if int(Entree[loop_d+6])==1 :
                                if int(Entree[loop_d+7])==1 :
                                    if int(Entree[loop_d+8])==1 :
                                        if int(Entree[loop_d+9])==1 :
                                            if int(Entree[loop_d+10])==1 :
                                                if int(Entree[loop_d+11])==1 :
                                                    Bls=Bls+[(loop_d)+13]

#Supression partie portant indicatifs

Erreur1=[]
Erreur2=[]
del Entree[-19:len(Entree)]

#supression des balises et ou des parties erronnées du message

for loop_f in range (1,len(Bls),1):
    del Entree[((Bls[loop_f])-14)-14*(loop_f-1):((Bls[loop_f]))-14*(loop_f-1)]
    Bls[loop_f]=Bls[loop_f]-14*loop_f
    if Bls[loop_f]-Bls[loop_f-1]!=65 :
        Erreur1.append(Bls[loop_f-1])
        Erreur2.append(Bls[loop_f])

for loop_g in range (len(Erreur1)):
    del Entree[Erreur1[loop_g]:Erreur2[loop_g]]

#Traduction et placement des caractères de la phrase

for loop_a in range (len(Entree)//13):
    a=int(Entree[13*loop_a+0])
    b=int(Entree[13*loop_a+1])
    c=int(Entree[13*loop_a+2])
    d=int(Entree[13*loop_a+3])
    e=int(Entree[13*loop_a+4])
    f=int(Entree[13*loop_a+5])
    g=int(Entree[13*loop_a+6])
    h=int(Entree[13*loop_a+7])
    i=int(Entree[13*loop_a+8])
    j=int(Entree[13*loop_a+9])
    k=int(Entree[13*loop_a+10])
    l=int(Entree[13*loop_a+11])
    m=int(Entree[13*loop_a+12])
    resultat[trad_7(a,b,c,d,e,f,g)]=str(dic(trad_6(h,i,j,k,l,m)))

message_chiffre=""
for loop_c in range (Bls[-1]//26):
    if resultat[loop_c] !='':
        message_chiffre=message_chiffre+resultat[loop_c]
    else:
        message_chiffre=message_chiffre+'/?/'


#2eme programme

import string
import time

#Définition clef

#private_key=str(input("Veuillez entrer votre clef : "))
private_key=input('Saisissez la clé de chiffrement: ')

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))

#Récupération du nombre de lettres à chiffrer dans le message pour définir le nombre de fois que nous avons besoin de la clé de chiffrement privée
# (+) Division du nombre de caractère par la longueur de la clé de chiffrement privée
#On ajoute 1 pour éviter 9/2 = 1 fois la clé au lieu de 2


def count_letters(msg):
    return len(msg)

msg = message_chiffre
key_repeat = int(count_letters(msg) / key_count) + 1
message_length = int(count_letters(msg))

#Définition de la liste de décalage à éxécuter (pour chaque lettre) en fonction de la clé privée, ex: abcabcabcabcabcabc

key_chain = private_key * key_repeat

#Envoi de la liste de décalage en chiffre dans un fichier txt et remplacement des a par 1, b par 2, etc ...
key_chain = key_chain.replace('A', '1\n')
key_chain = key_chain.replace('B', '2\n')
key_chain = key_chain.replace('C', '3\n')
key_chain = key_chain.replace('D', '4\n')
key_chain = key_chain.replace('E', '5\n')
key_chain = key_chain.replace('F', '6\n')
key_chain = key_chain.replace('G', '7\n')
key_chain = key_chain.replace('H', '8\n')
key_chain = key_chain.replace('I', '9\n')
key_chain = key_chain.replace('J', '10\n')
key_chain = key_chain.replace('K', '11\n')
key_chain = key_chain.replace('L', '12\n')
key_chain = key_chain.replace('M', '13\n')
key_chain = key_chain.replace('N', '14\n')
key_chain = key_chain.replace('O', '15\n')
key_chain = key_chain.replace('P', '16\n')
key_chain = key_chain.replace('Q', '17\n')
key_chain = key_chain.replace('R', '18\n')
key_chain = key_chain.replace('S', '19\n')
key_chain = key_chain.replace('T', '20\n')
key_chain = key_chain.replace('U', '21\n')
key_chain = key_chain.replace('V', '22\n')
key_chain = key_chain.replace('W', '23\n')
key_chain = key_chain.replace('X', '24\n')
key_chain = key_chain.replace('Y', '25\n')
key_chain = key_chain.replace('Z', '26\n')
key_chain_export = open('./resources/code/keychain.txt', 'w')
key_chain_export = key_chain_export.write(key_chain)

#Décalage des lettres selon la liste établie précedemment

def caesarize_letter(letter, shift):
    if 'A' <= letter.upper() <= 'Z':
        start = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def caesarize(text, shift):
    return ''.join([caesarize_letter(letter, shift) for letter in text])

def uncaesarize(text, shift):
    return ''.join([caesarize_letter(letter, -1 * shift) for letter in text])

message_dechiffre = ''
i = 0
for element in message_chiffre:
  with open("./resources/code/keychain.txt") as f:
    data = f.readlines()[i]
    data =  int(data)
    data = -data
    message_dechiffre = str(message_dechiffre) + (caesarize(element, data))
    i = i + 1

print('Voici le message déchiffré: ' + message_dechiffre)

#Vérification de l'intégrité du message

indicatif2 = 0

for i in message_dechiffre:
    if i == 'a' or i == 'A':
        indicatif2 = indicatif2 + 1
    if i == 'b' or i == 'B':
        indicatif2 = indicatif2 + 2
    if i == 'c' or i == 'C':
        indicatif2 = indicatif2 + 3
    if i == 'd' or i == 'D':
        indicatif2 = indicatif2 + 4
    if i == 'e' or i == 'E':
        indicatif2 = indicatif2 + 5
    if i == 'f' or i == 'F':
        indicatif2 = indicatif2 + 6
    if i == 'g' or i == 'G':
        indicatif2 = indicatif2 + 7
    if i == 'h' or i == 'H':
        indicatif2 = indicatif2 + 8
    if i == 'i' or i == 'I':
        indicatif2 = indicatif2 + 9
    if i == 'j' or i == 'J':
        indicatif2 = indicatif2 + 10
    if i == 'k' or i == 'K':
        indicatif2 = indicatif2 + 11
    if i == 'l' or i == 'L':
        indicatif2 = indicatif2 + 12
    if i == 'm' or i == 'M':
        indicatif2 = indicatif2 + 13
    if i == 'n' or i == 'N':
        indicatif2 = indicatif2 + 14
    if i == 'o' or i == 'O':
        indicatif2 = indicatif2 + 15
    if i == 'p' or i == 'P':
        indicatif2 = indicatif2 + 16
    if i == 'q' or i == 'Q':
        indicatif2 = indicatif2 + 17
    if i == 'r' or i == 'R':
        indicatif2 = indicatif2 + 18
    if i == 's' or i == 'S':
        indicatif2 = indicatif2 + 19
    if i == 't' or i == 'T':
        indicatif2 = indicatif2 + 20
    if i == 'u' or i == 'U':
        indicatif2 = indicatif2 + 21
    if i == 'v' or i == 'V':
        indicatif2 = indicatif2 + 22
    if i == 'w' or i == 'W':
        indicatif2 = indicatif2 + 23
    if i == 'x' or i == 'X':
        indicatif2 = indicatif2 + 24
    if i == 'y' or i == 'Y':
        indicatif2 = indicatif2 + 25
    if i == 'z' or i == 'Z':
        indicatif2 = indicatif2 + 26

indicatif2 = int(indicatif2)
secur2 = int(secur2)
renée2 = 0
if secur2 == indicatif2:
    renée2 = 0
else:
    renée2 = 1

longueur_message_dechiffre = len(message_dechiffre)

if longueur_message_dechiffre == int(indicatif) and indicatif2 == secur2:
    print('Message Complet 👌')
    time.sleep(3)
    print("Petit cadeau")
    time.sleep(2)
    print("          .")
    print("        ('")
    print("        '|")
    print("        |'")
    print("       [::]")
    print("       [::]   _......_")
    print("       [::].-'      _.-`.")
    print("       [:.'    .-. '-._.-`.")
    print("       [/ /\   |  \        `-..")
    print("       / / |   `-.'      .-.   `-.")
    print("      /  `-'            (   `.    `.")
    print("     |           /\      `-._/      \ ")
    print("     '    .'\   /  `.           _.-'|")
    print("    /    /  /   \_.-'        _.':;:/")
    print("  .'     \_/             _.-':;_.-'")
    print(" /   .-.             _.-' \;.-'")
    print("/   (   \       _..-'     |")
    print("\    `._/  _..-'    .--.  |")
    print(" `-.....-'/  _ _  .'    '.|")
    print("          | |_|_| |      | \  (o)")
    print("     (o)  | |_|_| |      | | (\'/)")
    print("     (\'/)/  ''''' |     o|  \;:;")
    print("     :;  |        |      |  |/)")
    print("      ;: `-.._    /__..--'\.' ;:")
    print("          :;  `--' :;   :;")
else:
    print('Message défectueux ❌')