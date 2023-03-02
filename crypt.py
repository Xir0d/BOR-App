import time
import string
from collections import Counter

#Easter Egg Lancement:

print('\033[0;33mLancement de BOR System®\033[0m' + ' ඞ')
time.sleep(3)
print('\033[1;31m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀')
print('⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀')
print('⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀')
print('⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀')
print('⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀')
print('⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀')
print('⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀')
print('⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀')
print('⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀')
print('⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁\033[0m')
time.sleep(1)


#Importation de la clé privée de codage
private_key = open('clé privé.key')
private_key = private_key.read()

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))

#Demande du message à chiffrer avec la clé privée
message_a_chiffrer = input("\033[92mÉcrivez le message à chiffrer: ")

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

message_chiffre = ''
i = 0
for element in message_a_chiffrer:
  with open("keychain.txt") as f:
    data = f.readlines()[i]
    message_chiffre = str(message_chiffre) + (caesarize(element, int(data)))
    i = i + 1

#Ajout du chiffre permettant de sécuriser l'authenticité du message:
longueur_message_chiffre = str(len(message_chiffre))
message_chiffre = message_chiffre + '-' + longueur_message_chiffre

#Affichage du Message final une fois chiffré et recomposé en ligne
print('\033[0mVoici le message chiffré: ', '\033[93m', message_chiffre, '\033[0m')