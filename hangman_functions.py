import random
import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Hangman():

    def __init__(self):
        pass

    def random_word():

        words = ["abete","biscotto","calamaro","delfino","elefante","fragola","giungla","hotel","ingranaggio","jeans","koala","labbra","montagna","neve","orologio","pennarello","quadro","razzo","serpente","tavolozza","uva","valigia","zucchero","arancia","bagnino","ciliegia","drago","elastico","formaggio","gabbiano","isola","lupo","mistero","notte","occhiali","puzzle","quaderno","robot","squalo","tromba","unicorno","volpe","zaino","burrone","ciambella","domino","esploratore","forbice","girasole","lanterna"]
        choosen_word = words[random.randint(0,len(words)-1)]

        return choosen_word

    def life_counter():

        lives_number = 0
        while True:

            difficulty = input("Scegli la difficoltà a cui vuoi giocare [Facile / Media / Difficile]: ")
            time.sleep(1)

            if difficulty.lower() == "facile":
                print("\nDifficoltà 'Facile' scelta! Hai a disposizione 5 vite!")
                lives_number = 5
                break

            elif difficulty.lower() == "media":
                print("\nDifficoltà 'Media' scelta! Hai a disposizione 4 vite!")
                lives_number = 4
                break

            elif difficulty.lower() == "difficile":
                print("\nDifficoltà 'Difficile' scelta! Hai a disposizione 3 vite!")
                lives_number = 3
                break
            else:
                print("\nDifficoltà inserita non valida!\n")
        
        return lives_number
    
    def figure(lives):

        if lives == 5:

            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
        elif lives == 4:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
        elif lives == 3:

            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            
        elif lives == 2:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     |\n"
                  "  |      \n"
                  "__|__\n")
        
        elif lives == 1:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "__|__\n")
            
        elif lives == 0:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
                        
    def game():

        word = Hangman.random_word()
        remaning_letter = len(word)
        lives = Hangman.life_counter()
        chsn = []

        while True:
            
            clear_screen()

            time.sleep(2)

            if len(chsn) != 0:
                print(f"Lettere già inserite: {chsn}")

            control = ""

            for letter in word:

                if letter in chsn:
                    control += letter
                else:
                    control += "_"

            print(control)

            print(f"\nVite rimaste: {lives}\n")

            Hangman.figure(lives)

            while True:
                choosen_letter = input("Inserisci una lettera: ")

                if choosen_letter in chsn:
                    print("\nLettera già inserita!\n")

                elif not isinstance(choosen_letter, str) or not choosen_letter.strip():
                    print("\nDev'essere inserita una stringa!\n")

                elif len(choosen_letter) != 1:
                    print("\nDevi inserire una singola lettera\n")

                elif not choosen_letter.isalpha():
                    print("\nDevi inserire una **lettera** dell'alfabeto!\n")

                else:
                    break

            time.sleep(1)

            if choosen_letter in word:

                print("\nComplimenti, la lettera è contenuta nella parola misteriosa!")
                remaning_letter -= word.count(choosen_letter)
                chsn.append(choosen_letter)
        
            else:

                print("\nParola errata!\n")
                lives -= 1
                chsn.append(choosen_letter)

            if remaning_letter == 0:
                print("\nHai vinto!\n")
                break

            if lives == 0:
                print(f"\nHai perso! La parole era {word}")
                break

            time.sleep(4)