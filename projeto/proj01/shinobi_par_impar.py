from random import random
from tkinter import *
from constantes import *
from calculo_par_impar import *
from reiniciar import restart_program
import tkinter.messagebox as msgbox


class Janela():
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()
        
        self.fr_result = Frame(raiz, bg=cinza1)
        self.fr_result.pack()
        
        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()
        
        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()
        
        self.fr4 = Frame(raiz, bg=cinza1)
        self.fr4.pack()
        
        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()
        
        self.fr6 = Frame(raiz, bg=cinza1)
        self.fr6.pack()
        
        self.image_player = PhotoImage(file="img/ninja.png")
        self.image_pc = PhotoImage(file="img/robo.png")
        self.img0 = PhotoImage(file="img/numero_0.png")
        self.img1 = PhotoImage(file="img/numero_1.png")
        self.img2 = PhotoImage(file="img/numero_2.png")
        self.img3 = PhotoImage(file="img/numero_3.png")
        self.img4 = PhotoImage(file="img/numero_4.png")
        self.img5 = PhotoImage(file="img/numero_5.png")
        self.img6 = PhotoImage(file="img/numero_6.png")
        self.img7 = PhotoImage(file="img/numero_7.png")
        self.img8 = PhotoImage(file="img/numero_8.png")
        self.img9 = PhotoImage(file="img/numero_9.png")
        self.img10 = PhotoImage(file="img/numero_10.png")
        
        self.lb1 = Label(self.fr1, text="Shinobi Par o Impar", bg=cinza1, font=fonte1, fg=azul2, pady=10, padx=35)
        self.lb1.pack(side="left")
        
        self.botao_restart = Button(self.fr1, text="Restart", command=self.resetar, font=fonte4, relief="raised")
        self.botao_restart.bind("<Return>", self.resetar2)
        self.botao_restart.pack(side="left")
        
        self.lb_result = Label(self.fr_result, text="", bg=cinza1, font=fonte1, fg="green")
        self.lb_result.pack()
        
        self.placar1 = 0
        self.placar2 = 0
        
        self.lb2 = Label(self.fr2, text=f"    Jogador         {self.placar1}  x  {self.placar2}      Computador", bg=cinza1, font=fonte3, fg=azul2, pady=10)
        self.lb2.pack()
        
        self.lb_img1 = Label(self.fr3, image=self.image_player, bg=cinza1)
        self.lb_img1.pack(side="left")
        
        self.lb_separador = Label(self.fr3, text="        ", bg=cinza1)
        self.lb_separador.pack(side="left")
        
        self.lb_img2 = Label(self.fr3, image=self.image_pc, bg=cinza1)
        self.lb_img2.pack(side="left")
        
        self.escolha = StringVar()
        
        self.rb_par = Radiobutton(self.fr4, text="Par", variable=self.escolha, value="par", bg=cinza1, font=fonte2, fg=azul2, pady=20)
        self.rb_par.pack(side="left")
        
        self.rb_impar = Radiobutton(self.fr4, text="Impar", variable=self.escolha, value="impar", bg=cinza1, font=fonte2, fg=azul2, pady=20)
        self.rb_impar.pack(side="left")
        
        self.lb3 = Label(self.fr5, text=f"Número de 0 à 10: ", bg=cinza1, font=fonte3, fg=azul2, width=15, pady=10)
        self.lb3.pack(side="left")
        
        self.num = Entry(self.fr5, width=2, font=fonte3)
        self.num.pack(side="left")
        
        self.bt_jogar = Button(self.fr6, text="Jogar", font=fonte1, fg=azul2, bg=cinza2, relief="raised", border=8, command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack()
        
        self.lb_erro = Label(self.fr6, text="", bg=cinza1, font=fonte4, fg="red")
        self.lb_erro.pack()
    
    
    def resetar(self):
        resposta = msgbox.askquestion("Restart", "Deseja reiniciar o jogo?")
        if resposta == "yes":
            restart_program()
        else:
            pass
    
    
    def resetar2(self, event):
        self.resetar()
    
    
    def jogar(self):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.ranrange(0, 11)

            if escolha == "par" or escolha == "impar":
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_img1["image"] = self.img0
                        self.lb_erro["text"] = ""
                    elif num == 1:
                        self.lb_img1["image"] = self.img1
                        self.lb_erro["text"] = ""
                    elif num == 2:
                        self.lb_img1["image"] = self.img2
                        self.lb_erro["text"] = ""
                    elif num == 3:
                        self.lb_img1["image"] = self.img3
                        self.lb_erro["text"] = ""
                    elif num == 4:
                        self.lb_img1["image"] = self.img4
                        self.lb_erro["text"] = ""
                    elif num == 5:
                        self.lb_img1["image"] = self.img5
                        self.lb_erro["text"] = ""
                    elif num == 6:
                        self.lb_img1["image"] = self.img6
                        self.lb_erro["text"] = ""
                    elif num == 7:
                        self.lb_img1["image"] = self.img7
                        self.lb_erro["text"] = ""
                    elif num == 8:
                        self.lb_img1["image"] = self.img8
                        self.lb_erro["text"] = ""
                    elif num == 9:
                        self.lb_img1["image"] = self.img9
                        self.lb_erro["text"] = ""
                    elif num == 10:
                        self.lb_img1["image"] = self.img10
                        self.lb_erro["text"] = ""
                    
                    if num_robo == 0:
                        self.lb_img2["image"] = self.img0
                        self.lb_erro["text"] = ""
                    elif num_robo == 1:
                        self.lb_img2["image"] = self.img1
                        self.lb_erro["text"] = ""
                    elif num_robo == 2:
                        self.lb_img2["image"] = self.img2
                        self.lb_erro["text"] = ""
                    elif num_robo == 3:
                        self.lb_img2["image"] = self.img3
                        self.lb_erro["text"] = ""
                    elif num_robo == 4:
                        self.lb_img2["image"] = self.img4
                        self.lb_erro["text"] = ""
                    elif num_robo == 5:
                        self.lb_img2["image"] = self.img5
                        self.lb_erro["text"] = ""
                    elif num_robo == 6:
                        self.lb_img2["image"] = self.img6
                        self.lb_erro["text"] = ""
                    elif num_robo == 7:
                        self.lb_img2["image"] = self.img7
                        self.lb_erro["text"] = ""
                    elif num_robo == 8:
                        self.lb_img2["image"] = self.img8
                        self.lb_erro["text"] = ""
                    elif num_robo == 9:
                        self.lb_img2["image"] = self.img9
                        self.lb_erro["text"] = ""
                    elif num_robo == 10:
                        self.lb_img2["image"] = self.img10
                        self.lb_erro["text"] = ""
                    
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == "par":
                        self.lb_result["text"] = "DEU PAR"
                    elif par_impar == "impar":
                        self.lb_result["text"] = "DEU IMPAR"
                    
                    if par_impar == "par" and escolha == "par":
                        self.placar1 += 1
                        self.lb2["text"] = f"    Jogador         {self.placar1}  x  {self.placar2}      Computador"
                    elif par_impar == "impar" and escolha == "impar":
                        self.placar1 += 1
                        self.lb2["text"] = f"    Jogador         {self.placar1}  x  {self.placar2}      Computador"
                    elif par_impar == "par" and escolha == "impar":
                        self.placar2 += 1
                        self.lb2["text"] = f"    Jogador         {self.placar1}  x  {self.placar2}      Computador"
                    elif par_impar == "impar" and escolha == "par":
                        self.placar2 += 1
                        self.lb2["text"] = f"    Jogador         {self.placar1}  x  {self.placar2}      Computador"
                    
                else:
                    self.lb_erro["text"] = "Erro escolha PAR ou IMPAR e um número de 0 à 10"
            else:
                self.lb_erro["text"] = "Erro escolha PAR ou IMPAR e um número de 0 à 10"

        except:
            self.lb_erro["text"] = "Erro escolha PAR ou IMPAR e um número de 0 à 10"
    
    
    def jogar2(self, event):
        self.jogar()


raiz = Tk()

raiz.geometry("840x650+300+30")
raiz.iconbitmap("img/ninjaa.ico")
raiz.title("Shinobi Par o Impar")
raiz["bg"] = cinza1

janela = Janela(raiz)

raiz.mainloop()
