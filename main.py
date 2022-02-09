from python_brasilidades.documento import Documento

#cpf = 15316264754
#objeto_cpf = CpfCnpj(cpf)
#print(objeto_cpf)

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documnto(exemplo_cnpj)
print(documento)


exemplo_cpf = "32007832062"
documento2 = Documento.cria_documnto(exemplo_cpf)
print(documento2)
