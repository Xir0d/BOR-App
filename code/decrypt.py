import string
import time
import subprocess
import json


#Définition des Variables:

message_chiffre = input('Message à décoder: ')
securite_1 = input('Sécurité 1: ')
securite_2 = input('Sécurité 2: ')

private_key = open('clé privé.key')
private_key = private_key.read()

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
key_chain_export = open('keychain.txt', 'w')
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
  with open("keychain.txt") as f:
    data = f.readlines()[i]
    data =  int(data)
    data = -data
    message_dechiffre = str(message_dechiffre) + (caesarize(element, data))
    i = i + 1

print('\033[92mVoici le message déchiffré: ' + '\033[93m' + message_dechiffre + '\033[0m')

#Vérification de l'intégrité du message
renée = 0
longueur_message_dechiffre = len(message_dechiffre)

renée = int(renée)
securite_2 = int(securite_2)
#Condition:

if securite_2 == longueur_message_dechiffre:
    renée = 0
else:
    renée = 1

#Definiton de la somme des valeur des lettres du message dans l'alphabet:

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
securite_1 = int(securite_1)
renée2 = 0
if securite_1 == indicatif2:
    renée2 = 0
else:
    renée2 = 1

if renée == 1 or renée2 == 1:
    print('\033[101mMessage défectueux ❌\033[0m')
    time.sleep(0.5)
    print('Vous êtes un plébéien, merci de retenter votre chance')
    time.sleep(1.5)
    print('Je vais relancer le programme pour vous')
    time.sleep(1.5)
    print('Vous êtes inutile, patientez 3 secondes pour la peine')
    time.sleep(3)
    subprocess.call(['python', 'decrypt.py'])
else:
    print('\033[102mMessage Complet 👌\033[0m')