from dados import Dados
class Livro (Dados):
    

    def __init__(self, titulo, autor, ano, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__genero = genero
    
    
    @classmethod
    def cadastrar(cls):
        print("Insira as informações para cadastrar o livro:")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        genero = input("Genero")

        livro = {
            "Titulo":titulo,
            "Autor":  autor,
            "Ano": ano,
            "Genero":genero
        }

        cls.adicionar(livro)

    @classmethod
    def listar(cls):
        lista = cls.carregar()
        for index, l in enumerate(lista):
            print(f"{index+1}º ------------")
            print(f"\t-Titulo:{l['Titulo']}")
            print(f"\t-Autor:  {l['Autor']}")
            print(f"\t-Ano: {l['Ano']}")
            print(f"\t-Genero:{l['Genero']}")
        print("Fim listagem....\n")



        


        
