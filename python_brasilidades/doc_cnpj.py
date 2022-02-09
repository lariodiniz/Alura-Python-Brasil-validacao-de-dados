from validate_docbr import CNPJ

class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
                self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def __str__(self):
        return self.formata()
