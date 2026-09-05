# Importa la libreria Tkinter con l'abbreviazione tk.
import tkinter as tk

# Importa il componente per visualizzare finestre di messaggio.
from tkinter import messagebox


# Definisce la funzione eseguita quando viene premuto il pulsante.
def show_welcome_message():
    # Mostra una finestra informativa con titolo e messaggio.
    messagebox.showinfo("Benvenuto", "Benvenuto nell'applicazione!")


# Definisce la funzione principale dell'applicazione.
def main():
    # Crea la finestra principale di Tkinter.
    window = tk.Tk()

    # Imposta il titolo della finestra.
    window.title("Main")

    # Imposta la dimensione della finestra in pixel.
    window.geometry("320x180")

    # Impedisce all'utente di ridimensionare la finestra.
    window.resizable(False, False)

    # Crea il pulsante che mostrera il messaggio di benvenuto.
    welcome_button = tk.Button(
        # Indica che il pulsante appartiene alla finestra principale.
        window,

        # Imposta il testo visualizzato sul pulsante.
        text="Mostra messaggio di benvenuto",

        # Collega il pulsante alla funzione da eseguire al click.
        command=show_welcome_message,
    )

    # Inserisce il pulsante nella finestra e lo centra nello spazio disponibile.
    welcome_button.pack(expand=True)

    # Avvia il ciclo principale che mantiene aperta la finestra.
    window.mainloop()


# Controlla che il file sia stato eseguito direttamente.
if __name__ == "__main__":
    # Avvia la funzione principale dell'applicazione.
    main()