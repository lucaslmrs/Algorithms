"""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   Crie uma lista que atua sobre um TAD. Para essa questão, considere que          *
*   queremos modelar uma lista encadeada de clientes de uma dada empresa. Para      *
*   isso, modele o dado Empresa (nomeEmpresa, listaClientes) e Cliente (nome ,cpf). *
*   Construa os seguintes métodos:                                                  *
*                                                                                   *
*   a) Adicionar um cliente a lista (um único cliente por cpf);                     *
*   b) Imprimir todos os dados de todos os clientes;                                *
*   c) Verificar se um cliente está contido na lista;                               *
*   d) Exibir o número de clientes cadastros.                                       *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
from list.ex_01.empresa import Company


a = Company('Microsoft')

print(a.n_registered_customers())

a.insert_customer('lucas', '988459045')
a.insert_customer('maria', '208353302')
a.insert_customer('vjack', '283720239')
a.show_custumers()

print(a.n_registered_customers())

print(a.contains('238728528327532759208575'))
print(a.contains('283720239'))

a.insert_customer('joao', '283720239')
a.show_custumers()
