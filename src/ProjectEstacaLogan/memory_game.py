import tkinter as tk
import random

# Initialiser les cartes (8 paires pour 16 cartes)
card_values = list(range(1, 9)) * 2  # 8 paires
random.shuffle(card_values)  # Mélanger les cartes

cards = card_values

# Configuration des paramètres du jeu
CARD_BACK = "❓"
PAIRS_COUNT = 8
CARDS = [f"🂡 {i+1}" for i in range(PAIRS_COUNT)] * 2  # 8 paires de cartes
random.shuffle(CARDS)

# Variables globales pour suivre l'état du jeu
revealed_cards = []
revealed_buttons = []
matches_found = 0

# Fonction de vérification des paires
def check_match():
    global revealed_cards, revealed_buttons, matches_found

    if len(revealed_cards) == 2:
        card1, card2 = revealed_cards
        button1, button2 = revealed_buttons

        if card1 == card2:
            matches_found += 1
            button1.config(state="disabled", bg="lightgreen")
            button2.config(state="disabled", bg="lightgreen")
        else:
            # Retourner les cartes après une pause
            root.after(1000, lambda: button1.config(text=CARD_BACK))
            root.after(1000, lambda: button2.config(text=CARD_BACK))

        # Réinitialiser l'état après vérification
        revealed_cards.clear()
        revealed_buttons.clear()

        # Vérifier si la partie est gagnée
        if matches_found == PAIRS_COUNT:
            win_label.config(text="Bravo ! Vous avez gagné 🎉", fg="green")

# Fonction pour retourner une carte
def reveal_card(button, card_value):
    if len(revealed_cards) < 2 and button["text"] == CARD_BACK:
        button.config(text=card_value)
        revealed_cards.append(card_value)
        revealed_buttons.append(button)
        check_match()

# Initialiser l'interface graphique
root = tk.Tk()
root.title("Jeu de Mémoire")
root.geometry("400x500")

# Titre
title_label = tk.Label(root, text="Jeu de Mémoire", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Plateau de jeu
game_frame = tk.Frame(root)
game_frame.grid(row=1, column=0, columnspan=4)

# Boutons pour les cartes
buttons = []
for row in range(4):
    button_row = []
    for col in range(4):
        card = cards.pop()
        # Crée un bouton pour chaque position
        btn = tk.Button(
            game_frame,  # Utilisation de game_frame pour éviter le conflit avec pack()
            text=CARD_BACK,  # Initialement, chaque carte est cachée
            width=10,
            height=5,
        )
        # Ajoute la commande pour révéler la carte
        btn.config(command=lambda b=btn, c=card: reveal_card(b, c))
        btn.grid(row=row, column=col)
        button_row.append(btn)
    buttons.append(button_row)

# Étiquette de victoire
win_label = tk.Label(root, text="", font=("Helvetica", 14))
win_label.grid(row=2, column=0, columnspan=4, pady=10)

# Bouton pour quitter
exit_button = tk.Button(root, text="Quitter", command=root.quit, bg="red", fg="white")
exit_button.grid(row=3, column=0, columnspan=4, pady=10)

# Lancer la boucle principale
root.mainloop()
