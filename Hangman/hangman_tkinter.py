import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["abete", "biscotto", "calamaro", "delfino", "elefante", "fragola", "giungla", "hotel",
         "ingranaggio", "jeans", "koala", "labbra", "montagna", "neve", "orologio", "pennarello",
         "quadro", "razzo", "serpente", "tavolozza", "uva", "valigia", "zucchero", "arancia",
         "bagnino", "ciliegia", "drago", "elastico", "formaggio", "gabbiano", "isola", "lupo",
         "mistero", "notte", "occhiali", "sardegna", "quaderno", "robot", "squalo", "tromba",
         "unicorno", "volpe", "zaino", "burrone", "ciambella", "domino", "esploratore", "forbice",
         "girasole", "lanterna"]

LIVES_MAP = {
    "Facile": 5,
    "Media": 4,
    "Difficile": 3
}

class HangmanGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gioco dell'impiccato")
        self.root.geometry("600x500")
        self.root.configure(bg="#f4f4f4")

        self.word = ""
        self.guessed_letters = []
        self.remaining_letters = 0
        self.lives = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Benvenuto al gioco dell'impiccato!", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
        self.title_label.pack(pady=10)

        self.diff_label = tk.Label(self.root, text="Scegli la difficoltà:", font=("Helvetica", 12), bg="#f4f4f4")
        self.diff_label.pack()

        self.diff_var = tk.StringVar()
        self.diff_menu = tk.OptionMenu(self.root, self.diff_var, *LIVES_MAP.keys())
        self.diff_menu.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Inizia Gioco", command=self.start_game, bg="#4caf50", fg="white", width=20)
        self.start_button.pack(pady=10)

        # Label per la visualizzazione del numero di vite rimanenti
        self.lives_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#f4f4f4")
        self.lives_label.pack(pady=5)

        self.word_label = tk.Label(self.root, text="", font=("Courier", 20), bg="#f4f4f4")
        self.word_label.pack(pady=15)

        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="#fff")
        self.canvas.pack(pady=10)

        self.input_label = tk.Label(self.root, text="Inserisci una lettera:", bg="#f4f4f4")
        self.input_entry = tk.Entry(self.root)
        self.submit_button = tk.Button(self.root, text="Prova", command=self.guess_letter)

        self.info_label = tk.Label(self.root, text="", fg="red", bg="#f4f4f4")
        self.guessed_label = tk.Label(self.root, text="", bg="#f4f4f4")

    def start_game(self):
        difficulty = self.diff_var.get()
        if not difficulty:
            messagebox.showwarning("Attenzione", "Seleziona una difficoltà!")
            return

        # Imposta le vite in base alla difficoltà scelta
        self.lives = LIVES_MAP[difficulty]
        self.word = random.choice(WORDS)
        self.guessed_letters = []
        self.remaining_letters = len(set(self.word))

        # Aggiorna la visualizzazione della parola e del disegno
        self.update_word_display()
        self.update_hangman()
        self.info_label.config(text="")
        self.guessed_label.config(text="Lettere inserite: ")
        # Mostra il numero delle vite rimanenti
        self.lives_label.config(text=f"Vite rimaste: {self.lives}")

        # Disabilita il menu a tendina della difficoltà durante la partita
        self.diff_menu.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

        self.input_label.pack()
        self.input_entry.pack()
        self.submit_button.pack(pady=5)
        self.info_label.pack()
        self.guessed_label.pack()

    def update_word_display(self):
        display = " ".join([l if l in self.guessed_letters else "_" for l in self.word])
        self.word_label.config(text=display)

    def update_hangman(self):
        self.canvas.delete("all")
        base = [(20, 180, 180, 180), (50, 180, 50, 20), (50, 20, 120, 20), (120, 20, 120, 40)]
        for line in base:
            self.canvas.create_line(*line, width=2)

        parts = [
            lambda: self.canvas.create_oval(100, 40, 140, 80, width=2),  # Testa
            lambda: self.canvas.create_line(120, 80, 120, 130, width=2),  # Corpo
            lambda: self.canvas.create_line(120, 90, 100, 110, width=2),  # Braccio sx
            lambda: self.canvas.create_line(120, 90, 140, 110, width=2),  # Braccio dx
            lambda: self.canvas.create_line(120, 130, 100, 160, width=2), # Gamba sx
            lambda: self.canvas.create_line(120, 130, 140, 160, width=2)  # Gamba dx
        ]

        errors = (5 - self.lives) + 1
        for i in range(errors):
            if i < len(parts):
                parts[i]()

    def guess_letter(self):
        letter = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if not letter or len(letter) != 1 or not letter.isalpha():
            self.info_label.config(text="Inserisci una singola lettera valida!")
            return

        if letter in self.guessed_letters:
            self.info_label.config(text="Hai già inserito questa lettera!", fg="red")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            self.remaining_letters = len([c for c in self.word if c not in self.guessed_letters])
            self.info_label.config(text="Lettera corretta!", fg="green")
        else:
            self.lives -= 1
            self.info_label.config(text="Lettera sbagliata!", fg="red")
        
        # Aggiorna la label delle vite rimanenti ad ogni mossa
        self.lives_label.config(text=f"Vite rimaste: {self.lives}")

        self.guessed_label.config(text="Lettere inserite: " + ", ".join(self.guessed_letters))
        self.update_word_display()
        self.update_hangman()

        if self.remaining_letters == 0:
            messagebox.showinfo("Hai vinto!", f"Hai indovinato la parola: {self.word}")
            self.reset()
        elif self.lives == 0:
            messagebox.showinfo("Hai perso!", f"La parola era: {self.word}")
            self.reset()

    def reset(self):
        self.word = ""
        self.word_label.config(text="")
        self.canvas.delete("all")
        self.input_label.pack_forget()
        self.input_entry.pack_forget()
        self.submit_button.pack_forget()
        self.info_label.pack_forget()
        self.guessed_label.pack_forget()

        # Riabilita la selezione della difficoltà per una nuova partita
        self.diff_menu.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.lives_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
