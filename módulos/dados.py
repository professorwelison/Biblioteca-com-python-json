import json, os

class Dados:
    _base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _arquivo = os.path.join(_base_path, "data", "dados.json")

    @classmethod
    def set_arquivo(cls, nome):
        if ".json" in nome:
            cls._arquivo = "/data/"+nome
        else:
            cls._arquivo = "/data/"+nome+".json"



    @classmethod
    def carregar(cls):
        try:
            with open(cls._arquivo, "r", encoding="UTF-8") as arquivo:
                dado = json.load(arquivo)
                return dado
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as e:
            print(f"Erro inesperado ao carregar dados: {str(e)}")
            return False
        
    @classmethod
    def salvar(cls, dado):
        try:
            with open(cls._arquivo, "w", encoding="UTF-8") as arquivo:
                json.dump(dado, arquivo, indent=4, ensure_ascii=False)
                return True
        except PermissionError:
            print(f"Erro: Sem permissão para escrever no arquivo '{cls._arquivo}'.")
            return False
        except Exception as e:
            print(f"Erro inesperado ao salvar dados: {str(e)}")
            return False
        
    @classmethod
    def adicionar(cls, dicionario):
        dados_arquivo = cls.carregar()

        try:
            dados_arquivo.append(dicionario)
        except TypeError:
            print(f"O tipo passado no parâmetro não é uma lista ou dicionário.\n {dicionario}")
        cls.salvar(dados_arquivo)
    

