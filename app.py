from customtkinter import *
from tkinter import *
from tkinter import messagebox
import tkinter

Janela = tkinter.Tk()

class App():
    def __init__(self):
        self.Tela()
        self.Tela_login_componentes()
        Janela.mainloop()
        

    def Tela(self):
        icon = tkinter.PhotoImage(file="C:/Users/lucas/Desktop/KANBAN/images/parcela.png")
        Janela.iconphoto(True, icon)
        Janela.state('zoomed')
        Janela.title("TAGTASK")

    
    def Tela_login_componentes(self):

        texto = "#545454"
        btn_color = "#00bf63"

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

        label_login = CTkLabel(Frame_login, text="------- Login -------", text_color = texto, font=("Roboto", 20))
        label_login.grid(column = 0, row = 1)

        # Entrys Login
        user_entry = CTkEntry(Frame_login, placeholder_text="Usuário", width=250, fg_color="#ccc", border_color="#191919", border_width=0.6,text_color="#000", placeholder_text_color="#000")
        user_entry.grid(column = 0, row = 2, pady = 10)

        password_entry = CTkEntry(Frame_login, placeholder_text="Senha", width=250, fg_color="#ccc", border_color="#191919", border_width=0.6,text_color="#000", placeholder_text_color="#000", show = "*")
        password_entry.grid(column = 0, row = 3, pady = 10)

        login_btn = CTkButton(Frame_login, text="ENTRAR", width=250, cursor = "hand2", fg_color= btn_color, text_color="#000", hover_color="#0f0")
        login_btn.grid(column = 0, row = 4, pady = 10)
        
        # Creditos label
        credito_label = CTkLabel(Frame_login, text="---- Desenvolvido por: Lucas Duarte ----", text_color = texto, font=("Roboto", 15))
        credito_label.grid(column = 0, row = 5, pady= 10)

        # Cadastro
        cadastro_label = CTkLabel(Frame_login, text="Não Tem Conta?:", text_color = texto, font=("Roboto", 13))
        cadastro_label.grid(column = 0, row = 7, pady= 10)

        def cadastro_tela():

            # Retirando Componentes Login
            Frame_login.pack_forget()

            cadastro_btn.pack_forget()
           
            # # Iserindo Componentes de Cadastro
            Frame_cadastro = CTkFrame(Janela, width=320, height=765, corner_radius=0, fg_color="transparent")
            Frame_cadastro.grid(column = 1, row= 0, padx=45, sticky= "N", pady= 130)

            # Logo Tag
            logo_task = tkinter.PhotoImage(file="C:/Users/lucas/Desktop/KANBAN/images/TagTask_Peq.png")

            label_logo = CTkLabel(Frame_cadastro, image=logo_task, text="")
            label_logo.grid(column = 0, row = 0)

            # Componentes Cadastro
            label_login = CTkLabel(Frame_cadastro, text="------- Cadastrar -------", text_color = texto, font=("Roboto", 20))
            label_login.grid(column = 0, row = 1)

            # Entrys cadastro
            user_entry = CTkEntry(Frame_cadastro, placeholder_text="Usuário", width=250, fg_color="#ccc", border_color="#191919", border_width=0.6,text_color="#000", placeholder_text_color="#000")
            user_entry.grid(column = 0, row = 2, pady = 10)

            password_entry = CTkEntry(Frame_cadastro, placeholder_text="Senha", width=250, fg_color="#ccc", border_color="#191919", border_width=0.6,text_color="#000", placeholder_text_color="#000", show = "*")
            password_entry.grid(column = 0, row = 3, pady = 10)

            password_entry_confirm = CTkEntry(Frame_cadastro, placeholder_text="Repita a Senha", width=250, fg_color="#ccc", border_color="#191919", border_width=0.6,text_color="#000", placeholder_text_color="#000", show = "*")
            password_entry_confirm.grid(column = 0, row = 4, pady = 10)

            def Verificar_Cadastro():

                try:

                    user = user_entry.get()
                    password = password_entry.get()
                    password_confirm = password_entry_confirm.get()

                    if user == "":
                        messagebox.showerror(title="Usuário Inválido", message="Insira Um Usuário Válido!")
                    if password == "":
                        messagebox.showerror(title="Usuário Inválido", message="Insira Uma senha Válida!")
                    if password == "":
                        messagebox.showerror(title="Usuário Inválido", message="Insira Uma senha Válida 2 !")
                    if password != password_confirm:
                        messagebox.showerror(title="Senhas Divergêntes", message="As senhas inseridas, não são iguais!")

                    else:
                        dados = [user, password, password_confirm]
                        messagebox.showinfo(title="Sucesso", message="Usuário Criado Com Sucesso!")
                except:
                    pass
                        

                

            cadastro_user_btn = CTkButton(Frame_cadastro, text="CADASTRAR", width=250, cursor = "hand2", fg_color= btn_color, text_color="#000", hover_color="#0f0", command= Verificar_Cadastro)
            cadastro_user_btn.grid(column = 0, row = 5, pady = 10)
            
            def voltar():
                # Retirando Frame Cadastro
                Frame_cadastro.destroy()

                # Devolvendo Botao Cadastro
                cadastro_btn.grid(column = 0, row = 8)
                pass

            voltar_btn = CTkButton(Frame_cadastro, text="VOLTAR", width=120, cursor = "hand2", fg_color= btn_color, text_color="#000", hover_color="#0f0", command= voltar)
            voltar_btn.grid(column = 0, row = 6, pady = 10)

            # Retirando botao de cadastro
            cadastro_btn.place(x = 10000, y = 10000)

            pass

        cadastro_btn = CTkButton(Frame_login, text="CADASTRE-SE", width=200, cursor = "hand2", fg_color= "#069", text_color="#000", hover_color="#0f0", command= cadastro_tela)
        cadastro_btn.grid(column = 0, row = 8)
    
    

App()