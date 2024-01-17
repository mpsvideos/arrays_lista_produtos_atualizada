"""
Curso: AWS
Turma: 20
Aluno: Marley Paranhos

Enunciado:
A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente!
Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons,
e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da
lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

Como desafio, adicione dois novos produtos da sua escolha à lista.
"""

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes',
                  'loções', 'xampus', 'sabonetes', 'delineadores'
                  ]

# imprimir cada produto no terminal
print('_' * 27)
print('*** LISTA DOS PRODUTOS ***')
print('_' * 27)
for i in lista_produtos:
    print(f'Temos {i} à venda!')


# atualizar produtos
# rímel ao invés de batons
lista_produtos[1] = 'rímel'

# cremes hidratantes no lugar de loções
lista_produtos[4] = 'hidratantes'

# ficaram sem delineadores
lista_produtos.pop()

# adicione dois novos produtos da sua escolha à lista
lista_produtos.append('condicionadores')
lista_produtos.append('depiladores')

# imprimir lista de produtos atualizada
print()
print('_' * 37)
print('*** LISTA DOS PRODUTOS ATUALIZADA ***')
print('_' * 37)
for i in lista_produtos:
    print(f'Temos {i} à venda!')
