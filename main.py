from python_brasilidades.documento import Documento
from python_brasilidades.telefones_br import TelefonesBr

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documnto(exemplo_cnpj)
print(documento)


exemplo_cpf = "32007832062"
documento2 = Documento.cria_documnto(exemplo_cpf)
print(documento2)

telefone = '552126481234'

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

