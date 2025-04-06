from colorama import init, Fore, Style
init()

class Usuário:
    def __init__ (self,nome,lista_livros_emprestados):
        self.nome = nome
        self.lista_livros_emprestados = lista_livros_emprestados

class Livros:
    def __init__ (self):
        self.livros = {}

    def Adicionar_livros_a_biblioteca(self,codigo,titulo,autor,emprestado):
        self.livros[codigo] = {"titulo":titulo,"autor":autor,"emprestado":emprestado}

    def Deletar_livros_da_biblioteca(self,codigo):
        del self.livros[codigo]

    def Exibir_todos_os_livros_da_biblioteca (self):
        for chave,valor in self.livros.items():
            Emprestado_ou_nao = ""
            if valor["emprestado"] == True:
                Emprestado_ou_nao = (Fore.RED + "Livro não está disponível para empréstimo"+Style.RESET_ALL)
            else:
                Emprestado_ou_nao = (Fore.GREEN + "Livro está disponível para empréstimo"+Style.RESET_ALL)
            print(f"{chave} - {valor["titulo"]} - {valor["autor"]} - {Emprestado_ou_nao}")
                

    def Pegar_livro_emprestado(self,codigo):
        
        if self.livros[codigo]["emprestado"] == False:
            self.livros[codigo]["emprestado"] = True
            print (f"Você pegou o livro {self.livros[codigo]["titulo"]} emprestado")
        else:
            print("Este livro já foi emprestado para outra pessoa")
        print("Lista de livros atualizada:")
        self.Exibir_todos_os_livros_da_biblioteca()

    def Devolver_livro_para_a_biblioteca (self,codigo):
        if self.livros[codigo]["emprestado"] == True:
            self.livros[codigo]["emprestado"] = False
            print(f"Agracemos a sua devolução. O livro {self.livros[codigo]["titulo"]} foi devolvido")        
        else:        
            print("Acho que houve um engano, este livro ainda está em nossa posse")
        print("Lista de livros atualizada:")
        self.Exibir_todos_os_livros_da_biblioteca()
    
           
livro = Livros()
livro.Adicionar_livros_a_biblioteca(0,"Pequeno Princípe","Antoine de Saint-Exupéry",True)
livro.Adicionar_livros_a_biblioteca(1,"Apologia à Socrátes","Platão",False)
livro.Adicionar_livros_a_biblioteca(2,"Hábitos atômicos","James Clear",False)

def Perguntar_ao_usuario_o_que_deseja_realizar():
    Acao_que_usuario_deseja_realizar = int(input(Fore.YELLOW +"Qual ação deseja realizar? Digite apenas o número da ação desejada\n"+Style.RESET_ALL+" 1 - Ver livros disponíveis na biblioteca\n 2 - Pegar um livro emprestado\n 3 - Devolver um Livro\n 4 - Finalizar \n"))
    return Acao_que_usuario_deseja_realizar
Acao_que_usuario_deseja_realizar = Perguntar_ao_usuario_o_que_deseja_realizar()

while Acao_que_usuario_deseja_realizar != 4:

    if Acao_que_usuario_deseja_realizar == 1: #Ver livros disponíveis na biblioteca
        livro.Exibir_todos_os_livros_da_biblioteca()
    elif Acao_que_usuario_deseja_realizar == 2: #Pegar um livro emprestado
        livro.Exibir_todos_os_livros_da_biblioteca()
        livro.Pegar_livro_emprestado(int(input("Digite o código do livro que deseja pegar emprestado:\n")))
    elif Acao_que_usuario_deseja_realizar == 3: #Devolver um livro
        livro.Exibir_todos_os_livros_da_biblioteca()
        livro.Devolver_livro_para_a_biblioteca(int(input("Digite o código do livro que deseja devolver:\n")))
    Acao_que_usuario_deseja_realizar = Perguntar_ao_usuario_o_que_deseja_realizar()






# Aprender a usar excessão
# Perguntar se você é usuário ou "dono"