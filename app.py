from customtkinter import *
from tkinter import *
import tkinter

Janela = tkinter.Tk()

class App():
    def __init__(self):
        self.Tela_login()
        self.Tela_login_componentes()
        Janela.mainloop()
        

    def Tela_login(self):
        icon = tkinter.PhotoImage(file="C:/Users/lucas/Desktop/KANBAN/images/parcela.png")
        Janela.iconphoto(True, icon)
        Janela.state('zoomed')
        Janela.title("TAGTASK")

    def Tela_login_componentes(self):

        texto = "#545454"
        image_login = tkinter.PhotoImage(file="C:/Users/lucas/Desktop/KANBAN/images/fundo_login.png")

        #Verde => #00bf63
        #texo => #545454

        # Frame Login Image
        Frame_image = CTkFrame(Janela, width=750, height=700, corner_radius=0)
        Frame_image.grid(column = 0, row= 0)

        Frame_login = CTkFrame(Janela, width=320, height=765, corner_radius=0, fg_color="transparent")
        Frame_login.grid(column = 1, row= 0, padx=45, sticky= "N", pady= 130)

        label_image = CTkLabel(Frame_image, image= image_login, width=1, height=1, text="")
        label_image.grid(column= 0, row = 0)

        # Logo Tag
        logo_task = tkinter.PhotoImage(file="C:/Users/lucas/Desktop/KANBAN/images/TagTask_Peq.png")

        label_logo = CTkLabel(Frame_login, image=logo_task, text="")
        label_logo.grid(column = 0, row = 0)

        # Componentes Login

        label_login = CTkLabel(Frame_login, text="Fazer Login", text_color = texto, font=("Roboto", 20))
        label_login.grid(column = 0, row = 1)

        # Entrys Login
        user_entry = CTkEntry(Frame_login, placeholder_text="Usuário", width=250)
        user_entry.grid(column = 0, row = 2, pady = 10)
        


App()