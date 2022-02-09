from python_brasilidades.doc_cnpj import DocCnpj
from python_brasilidades.doc_cpf import DocCpf

class Documento:

    @staticmethod
    def cria_documnto(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)

        else:
            raise ValueError("Quantidade de digito incorreta!")