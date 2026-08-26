import tkinter as tk

# Créez une fenêtre avec :
# - Un titre "Gestion des salles"
# - Un label qui affiche "Salle B-107"
# - Un label qui affiche "Capacité : 30 places"
# - Un bouton "Quitter" qui ferme la fenêtre

app = tk.Tk()
app.title("Gestion des salles")
label_salle = tk.Label(app, text="Salle B-107")
label_capacite = tk.Label(app, text="Capacité : 30 places")



bouton = tk.Button(app, text="Quitter", command=app.quit)
bouton.pack()
app.mainloop()









