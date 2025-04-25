import google.generativeai as genai
import os
import time
from datetime import datetime
from config import API_KEY_PRIVATE

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_conversation_file():
    # Crea una directory per le conversazioni se non esiste
    if not os.path.exists("gemini_conversations"):
        os.makedirs("gemini_conversations")
    
    # Genera un nome file basato sulla data e ora attuale
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gemini_conversations/conversation_{timestamp}.txt"
    
    # Crea e restituisci il file aperto in modalità scrittura
    return open(filename, "w", encoding="utf-8")

API_KEY = API_KEY_PRIVATE
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Crea un nuovo file per la conversazione corrente
conversation_file = create_conversation_file()

# Scrivi l'intestazione nel file
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
conversation_file.write(f"Gemini Chat - {current_date}\n")
conversation_file.write("="*50 + "\n\n")

clear_screen()
print("Chat with Gemini! Type 'exit' to quit.")

try:
    while True:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_input = input(f"({current_date}) You: ")
        if user_input.lower() == 'exit':
            break
        
        # Salva l'input dell'utente nel file
        conversation_file.write(f"({current_date}) You: {user_input}\n\n")
        
        # Invia il messaggio al modello
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = chat.send_message(user_input)
        
        # Stampa e salva la risposta
        print(f"({current_date}) Gemini:", response.text)
        conversation_file.write(f"({current_date}) Gemini: {response.text}\n\n")
        # Assicurati che il contenuto venga scritto immediatamente nel file
        conversation_file.flush()

finally:
    # Chiudi il file quando si esce dal programma
    if conversation_file:
        conversation_file.close()
        print(f"\nConversazione salvata in {conversation_file.name}")

time.sleep(3)
clear_screen()