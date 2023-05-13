import time
import string
from collections import Counter
import json

#Importation de la clé privée de codage
with open('code/data.json') as json_file:
    data = json.load(json_file)

private_key = data['cleDeChiffrement']

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))

#Demande du message à chiffrer avec la clé privée
message_a_chiffrer = data['messageAChiffrer']

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

#Ajout du premier indicatif:
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


#Définition de la variable message_chiffre_tempo :
message_chiffre_tempo = ""

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

i = 0
for element in message_a_chiffrer:
  with open("code/keychain.txt") as f:
    data = f.readlines()[i]
    message_chiffre_tempo = str(message_chiffre_tempo) + (caesarize(element, int(data)))
    i = i + 1

#Enlevement des indicatifs pour transcription du message :
message_transcription = message_chiffre_tempo

#Ajout du 1er indicatif :
indicatif = str(indicatif)
message_chiffre = ''
message_chiffre = message_chiffre + indicatif + '-'

#Retour à la normale :
message_chiffre = message_chiffre + message_chiffre_tempo

#Ajout du 2eme indicatif :
indicatif2 = 0
indicatif2 = str(indicatif2)
longueur_message_chiffre = int(len(message_chiffre)) - int(len(indicatif2)) - 1
longueur_message_chiffre = str(longueur_message_chiffre)
message_chiffre = message_chiffre + '-' + longueur_message_chiffre
indicatif2 = longueur_message_chiffre

#Affichage du Message final une fois chiffré et recomposé en ligne
print('\033[0mVoici le message chiffré: ', '\033[93m', message_chiffre, '\033[0m')

#Transcription du message chiffré dans le fichier data.json :
transcription = {
    "message": message_transcription,
    "indicatif1": indicatif,
    "indicatif2": indicatif2
}

with open('code/data.json', 'w') as f:
    json.dump(transcription, f)
