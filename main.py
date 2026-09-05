import tkinter as tk
from tkinter import messagebox


def show_welcome_message():
    messagebox.showinfo("Benvenuto", "Benvenuto nell'applicazione!")


def main():
    window = tk.Tk()
    window.title("Main")
    window.geometry("320x180")
    window.resizable(False, False)

    welcome_button = tk.Button(
        window,
        text="Mostra messaggio di benvenuto",
        command=show_welcome_message,
    )
    welcome_button.pack(expand=True)

    window.mainloop()


if __name__ == "__main__":
    main()