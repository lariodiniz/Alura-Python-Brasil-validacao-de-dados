import requests

class BuscaEndereco:

    def __init__(self, cep:str) -> None:
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self) -> str:
        return self.format_cep()

    def cep_e_valido(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf'],
        )
