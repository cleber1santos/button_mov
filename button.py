import tkinter as tk # biblioteca gráfica
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc") # função do buttão, tamanho e largura
b = ttk.Button(root, text="VOCÊ CLICOU !!")

def move(i):
    if i <= 50:
        b.place(x=i, y=i)
        root.after(100, lambda: move(i+1))

move(0)  # Inicia a animação imediatamente

root.mainloop()
