from python_brasilidades.documento import Documento
from python_brasilidades.telefones_br import TelefonesBr
from python_brasilidades.datas_br import DatasBr
from python_brasilidades.acesso_cep import BuscaEndereco
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documnto(exemplo_cnpj)
#print(documento)


exemplo_cpf = "32007832062"
documento2 = Documento.cria_documnto(exemplo_cpf)
#print(documento2)

telefone = '552126481234'

telefone_objeto = TelefonesBr(telefone)
#print(telefone_objeto)

cadastro = DatasBr()
#print(cadastro)
#print(cadastro.mes_cadastro())
#print(cadastro.dia_semana())

#print(cadastro.tempo_cadastro())

cep = '01001000'

busca = BuscaEndereco(cep)
print(busca)
bairro, cidade, uf = busca.acessa_via_cep()
print(bairro, cidade, uf)