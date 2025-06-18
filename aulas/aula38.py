# ---------------------------------------------------------------------------------------------
# Tkinter

import tkinter as tk

class Janela():  
    def __init__(self, raiz):
        self.img = tk.PhotoImage(file="aula38.png") # cria uma imagem
        
        self.fr1 = tk.Frame(raiz, bg="#333333") # cria um frame
        self.fr1.pack() # coloca o frame na janela (sempre que criar um objeto tem que empacotar)
        
        self.lb1 = tk.Label(self.fr1, text="Olá mundo!", background="#f56499", font=("Sans-Serif", 20, "bold", "italic")) # escreve "Olá mundo!"" no frame
        self.lb1.pack(side="left") # coloca o label no frame
        
        self.fr2 = tk.Frame(raiz, bg="#333333")
        self.fr2.pack()
        
        self.bt1 = tk.Button(self.fr2, text="Clique aqui", background="#f56475", font=("Sans-Serif", 20, "bold"), command=self.muda_label) # cria um botão
        self.bt1["relief"] = "raised"
        self.bt1["border"] = 10
        self.bt1.bind("<Return>", self.muda_label2) # quando apertar enter, chama a função muda_label
        self.bt1.pack(side="bottom") # coloca o botão no frame

    
    def muda_label(self):
        self.lb1["text"] = "Deu certo!"
        self.lb_img = tk.Label(raiz, image=self.img)
        self.lb_img.pack()
    
    def muda_label2(self, event):
        self.lb1["text"] = "Deu certo com o teclado tb!"
        self.lb_img = tk.Label(raiz, image=self.img)
        self.lb_img.pack()


raiz = tk.Tk() # cria uma janela
Janela(raiz)
raiz.geometry("500x300+1000+200") # largura x altura + posição x + posição y
raiz.title("Aula 38") # título da janela
# raiz.iconbitmap("aula38.ico") # ícone da janela
# raiz.overrideredirect(True) # tira a barra de título
raiz["bg"] = "#333333"

raiz.tk.mainloop() # executa a janela

