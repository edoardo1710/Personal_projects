import random
import time
import os

from hangman_functions import Hangman, clear_screen

clear_screen()

print("\nBenvenuto al gioco dell'impiccato\n")
nome = input("Inserisci il tuo nome: ")
time.sleep(1)
print("Benvenuto " + nome + "!\nIl gioco sta per cominciare, buona fortuna!\n")
time.sleep(2)

Hangman.game()

