import re

class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Telefone não encontrado!')

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
    
    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        ddi = resposta.group(1)
        ddd = resposta.group(2)
        numero1=resposta.group(3)
        numero2=resposta.group(4)
        numero_formatado =f'+{ddi}({ddd}){numero1}-{numero2}'
        
        return numero_formatado

    def __str__(self):
        return self.format_numero()