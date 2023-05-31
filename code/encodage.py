import time
import sys
import string
from collections import Counter

#Demande du message à chiffrer avec la clé privée et rajout de " " pour avoir un len/5

message_a_chiffrer = input("Écrivez le message à chiffrer: ")
if (len(message_a_chiffrer)%5)!=0:
    for i in range (5-(len(message_a_chiffrer)%5)):
        message_a_chiffrer=message_a_chiffrer+" "

#Importation de la clé privée de codage

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

msg = message_a_chiffrer
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
key_chain_export = open('code/keychain.txt', 'w')
key_chain_export = key_chain_export.write(key_chain)

#Indicatif deux

indicatif = 0
indicatif = int(indicatif)

for i in message_a_chiffrer:
    if i == 'a' or i == 'A':
        indicatif = indicatif + 1
    if i == 'b' or i == 'B':
        indicatif = indicatif + 2
    if i == 'c' or i == 'C':
        indicatif = indicatif + 3
    if i == 'd' or i == 'D':
        indicatif = indicatif + 4
    if i == 'e' or i == 'E':
        indicatif = indicatif + 5
    if i == 'f' or i == 'F':
        indicatif = indicatif + 6
    if i == 'g' or i == 'G':
        indicatif = indicatif + 7
    if i == 'h' or i == 'H':
        indicatif = indicatif + 8
    if i == 'i' or i == 'I':
        indicatif = indicatif + 9
    if i == 'j' or i == 'J':
        indicatif = indicatif + 10
    if i == 'k' or i == 'K':
        indicatif = indicatif + 11
    if i == 'l' or i == 'L':
        indicatif = indicatif + 12
    if i == 'm' or i == 'M':
        indicatif = indicatif + 13
    if i == 'n' or i == 'N':
        indicatif = indicatif + 14
    if i == 'o' or i == 'O':
        indicatif = indicatif + 15
    if i == 'p' or i == 'P':
        indicatif = indicatif + 16
    if i == 'q' or i == 'Q':
        indicatif = indicatif + 17
    if i == 'r' or i == 'R':
        indicatif = indicatif + 18
    if i == 's' or i == 'S':
        indicatif = indicatif + 19
    if i == 't' or i == 'T':
        indicatif = indicatif + 20
    if i == 'u' or i == 'U':
        indicatif = indicatif + 21
    if i == 'v' or i == 'V':
        indicatif = indicatif + 22
    if i == 'w' or i == 'W':
        indicatif = indicatif + 23
    if i == 'x' or i == 'X':
        indicatif = indicatif + 24
    if i == 'y' or i == 'Y':
        indicatif = indicatif + 25
    if i == 'z' or i == 'Z':
        indicatif = indicatif + 26

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

message_chiffre = ''
i = 0
for element in message_a_chiffrer:
  with open("code/keychain.txt") as f:
    data = f.readlines()[i]
    message_chiffre = str(message_chiffre) + (caesarize(element, int(data)))
    i = i + 1

#Ajout du chiffre permettant de sécuriser l'authenticité du message:

longueur_message_chiffre = str(len(message_chiffre))

#2eme programme

from random import shuffle

if len(message_chiffre)>128:
    sys.exit("Message trop long (128 caractères max)")

#Traduction nombre en série de 6 bits

def trad_6bites (ch_6):
    if ch_6>63:
        print("tg")
    elif ch_6<0:
        print("tg")
    else:
        if ch_6>=32:
            cha=1
            ch_6=ch_6-32
        else:
            cha=0
        if ch_6>=16:
            chb=1
            ch_6=ch_6-16
        else:
            chb=0
        if ch_6>=8:
            chc=1
            ch_6=ch_6-8
        else:
            chc=0
        if ch_6>=4:
            chd=1
            ch_6=ch_6-4
        else:

            chd=0
        if ch_6>=2:
            che=1
            ch_6=ch_6-2
        else:
            che=0
        if ch_6>=1:
            chf=1
            ch_6=ch_6-1
        else:
            chf=0
        Ret=[chf,che,chd,chc,chb,cha]
        return(Ret)

#Traduction place chaque caractère en série de 7 bits

def trad_7bites (ch_7):
    if ch_7>127:
        print("tg")
    elif ch_7<0:
        print("tg")
    else:
        if ch_7>=64:
            cha=1
            ch_7=ch_7-64
        else:
            cha=0
        if ch_7>=32:
            chb=1
            ch_7=ch_7-32
        else:
            chb=0
        if ch_7>=16:
            chc=1
            ch_7=ch_7-16
        else:
            chc=0
        if ch_7>=8:
            chd=1
            ch_7=ch_7-8
        else:
            chd=0
        if ch_7>=4:
            che=1
            ch_7=ch_7-4
        else:
            che=0
        if ch_7>=2:
            chf=1
            ch_7=ch_7-2
        else:
            chf=0
        if ch_7>=1:
            chg=1
            ch_7=ch_7-1
        else:
            chg=0
        return[chg,chf,che,chd,chc,chb,cha]

#Association caractère phrase codée à un nombre

Entree=message_chiffre#Correspondance entre codes des deux programmes
Entree=Entree.lower()
Seq=[]
Rang=0
for loop_a in range (len(Entree)):
    if (Entree[loop_a])==" " :
        Seq=Seq+[0]
    elif (Entree[loop_a])=="u" :
        Seq=Seq+[1]
    elif (Entree[loop_a])=="j" :
        Seq=Seq+[2]
    elif (Entree[loop_a])=="," :
        Seq=Seq+[3]
    elif (Entree[loop_a])==")" :
        Seq=Seq+[4]
    elif (Entree[loop_a])=="t" :
        Seq=Seq+[5]
    elif (Entree[loop_a])=="b" :
        Seq=Seq+[6]
    elif (Entree[loop_a])=="ç" :
        Seq=Seq+[7]
    elif (Entree[loop_a])=="m" :
        Seq=Seq+[8]
    elif (Entree[loop_a])=="e" :
        Seq=Seq+[9]
    elif (Entree[loop_a])=="-" :
        Seq=Seq+[10]
    elif (Entree[loop_a])=="2" :
        Seq=Seq+[11]
    elif (Entree[loop_a])=="r" :
        Seq=Seq+[12]
    elif (Entree[loop_a])=="'" :
        Seq=Seq+[13]
    elif (Entree[loop_a])=="9" :
        Seq=Seq+[14]
    elif (Entree[loop_a])=="=" :
        Seq=Seq+[15]
    elif (Entree[loop_a])=="3" :
        Seq=Seq+[16]
    elif (Entree[loop_a])=="@" :
        Seq=Seq+[17]
    elif (Entree[loop_a])=="s" :
        Seq=Seq+[18]
    elif (Entree[loop_a])=="4" :
        Seq=Seq+[19]
    elif (Entree[loop_a])=="/" :
        Seq=Seq+[20]
    elif (Entree[loop_a])=="v" :
        Seq=Seq+[21]
    elif (Entree[loop_a])=="!" :
        Seq=Seq+[22]
    elif (Entree[loop_a])=="(" :
        Seq=Seq+[23]
    elif (Entree[loop_a])=="i" :
        Seq=Seq+[24]
    elif (Entree[loop_a])=="+" :
        Seq=Seq+[25]
    elif (Entree[loop_a])=="è" :
        Seq=Seq+[26]
    elif (Entree[loop_a])=="o" :
        Seq=Seq+[27]
    elif (Entree[loop_a])=="à" :
        Seq=Seq+[28]
    elif (Entree[loop_a])==":" :
        Seq=Seq+[29]
    elif (Entree[loop_a])=="é" :
        Seq=Seq+[30]
    elif (Entree[loop_a])=="c" :
        Seq=Seq+[31]
    elif (Entree[loop_a])=="l" :
        Seq=Seq+[32]
    elif (Entree[loop_a])=="1" :
        Seq=Seq+[33]
    elif (Entree[loop_a])=="<" :
        Seq=Seq+[34]
    elif (Entree[loop_a])=="f" :
        Seq=Seq+[35]
    elif (Entree[loop_a])=="g" :
        Seq=Seq+[36]
    elif (Entree[loop_a])=="÷" :
        Seq=Seq+[37]
    elif (Entree[loop_a])=="h" :
        Seq=Seq+[38]
    elif (Entree[loop_a])=="0" :
        Seq=Seq+[39]
    elif (Entree[loop_a])=="a" :
        Seq=Seq+[40]
    elif (Entree[loop_a])==";" :
        Seq=Seq+[41]
    elif (Entree[loop_a])=="z" :
        Seq=Seq+[42]
    elif (Entree[loop_a])=="²" :
        Seq=Seq+[43]
    elif (Entree[loop_a])=='"':
        Seq=Seq+[44]
    elif (Entree[loop_a])=="y" :
        Seq=Seq+[45]
    elif (Entree[loop_a])=="ù" :
        Seq=Seq+[46]
    elif (Entree[loop_a])=="q" :
        Seq=Seq+[47]
    elif (Entree[loop_a])=="5" :
        Seq=Seq+[48]
    elif (Entree[loop_a])=="n" :
        Seq=Seq+[49]
    elif (Entree[loop_a])=="." :
        Seq=Seq+[50]
    elif (Entree[loop_a])=="k" :
        Seq=Seq+[51]
    elif (Entree[loop_a])=="x" :
        Seq=Seq+[52]
    elif (Entree[loop_a])=="p" :
        Seq=Seq+[53]
    elif (Entree[loop_a])=="8" :
        Seq=Seq+[54]
    elif (Entree[loop_a])=="ß" :
        Seq=Seq+[55]
    elif (Entree[loop_a])=="d" :
        Seq=Seq+[56]
    elif (Entree[loop_a])=="7" :
        Seq=Seq+[57]
    elif (Entree[loop_a])=="6" :
        Seq=Seq+[58]
    elif (Entree[loop_a])=="w" :
        Seq=Seq+[59]
    elif (Entree[loop_a])=="*" :
        Seq=Seq+[60]
    elif (Entree[loop_a])=="?" :
        Seq=Seq+[61]
    elif (Entree[loop_a])=="%" :
        Seq=Seq+[62]


#Regroupement caractère et sa place puis mélange + ajout nombre de caractères

Place=[]
F=[]
for loop_b in range (len(Seq)):
    Inter=""
    Trad=trad_6bites(Seq[loop_b])
    Place=trad_7bites(loop_b)
    for loop_bb in range (7):
        Inter=Inter+str(Place[loop_bb])
    for loop_bc in range (6):
        Inter=Inter+str(Trad[loop_bc])
    F=F+[Inter]
F=F+F
shuffle(F)

#code des securitées en 7 et 12 bits puis ajout à la fin de la soupe de bits

Inter_b=""
I1=0
I2=0

I1=trad_6bites(indicatif%64)
I2=trad_6bites(indicatif//64)


for loop_e in range (6):
    Inter_b=Inter_b+str(I1[loop_e])
for loop_e in range (6):
    Inter_b=Inter_b+str(I2[loop_e])

longueur_message_chiffre=trad_7bites(int(longueur_message_chiffre))

for loop_d in range (7):
    Inter_b=Inter_b+str(longueur_message_chiffre[loop_d])

#print final

R=0
for loop_c in range (len(F)):
    print (F[loop_c],end="")
    R=R+1
    if R==5 :
        print("01111111111110",end="")
        R=0

print(Inter_b)