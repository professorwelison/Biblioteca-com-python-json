from livro import Livro

def menu():
    while True:
        print("""
        #========== 🔢 MENU 🔢 ==========#
        1 - Cadastrar
        2 - Listar
        3 - Sair
        """)
        op = input()

        if op == "1":
            Livro.cadastrar()
            print("Cadastrando ...")
        elif op == "2":
            print("Listando ...")
            Livro.listar()
        elif op == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()