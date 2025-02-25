import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface Tkinter")
janela.geometry("300x200")

# Criando um botão
botao = tk.Button(janela, text="Clique Aqui!", command=lambda: print("Botão clicado!"))
botao.pack(pady=20)

# Iniciando a aplicação
janela.mainloop()
