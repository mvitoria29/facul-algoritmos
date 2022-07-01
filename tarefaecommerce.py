#elaborar sistema de controle de estoque para um e-commerce
#Criar funções para itens cadastrar, consultar, e remover peças
#Adicionar uma opção de encerramento do programa
print('Bem vindo ao controle de estoque do e-commerce de Maria Vitória - RU 3975516')
listapecas = []



#----------------COMECO cadastrarpeca---------------
def cadastrarpeca(cp):
    print('bem vindo ao menu de cadastro de peças')
    print('O código da nova peça é {}.' .format(cp))
    nome = input('Qual é o nome da peça? ')
    fabricante = input('Qual é o fabricante da peça? ')
    valor = input('Qual é o valor da peça?')
    dicionarioPeca = {'codigo' : cp, 'nome' : nome, 'fabricante' : fabricante, 'valor' : valor}
    listapecas.append(dicionarioPeca.copy())
#-------------------------FIM cadastrarpeca--------------




#---------------INICIO consultarpeca---------------------------
def consultarpeca():
    print('bem vindo ao menu de consulta de peças')
    while True:
        try:
            x = int(input('Digite a opção desejada:\n '
                          '1 - Consultar todas as peças\n '
                          '2 - Consultar peças por código\n '
                          '3 - Consultar peças por fabricante\n'
                          ' 4 - Retornar\n >>'))
            if x == 1:
                print('Consultar todos')
                for peca in listapecas:
                    for key, value in peca.items():
                        print('{}: {}' .format(key, value))
            elif x == 2:
                print('Consultar por código da peça')
                entrada = int(input('Digite o código da peça: '))
                for peca in listapecas:
                    if(peca['codigo'] == entrada):
                        for key, value in peca.items():
                            print('{}: {}'.format(key, value))
            elif x == 3:
                print('Consultar por fabricante')
                entrada = input('Digite o fabricante da peça: ')
                for peca in listapecas:
                    if(peca['fabricante'] == entrada):
                        for key, value in peca.items():
                            print('{}: {}'.format(key, value))
            elif x == 4:
                return
            else:
                print('Opção inválida')
        except ValueError:
            print('Valor inválido. Digite apenas números inteiros')

#------------------- FIM consultarpeca-----------------------------



#--------------------INICIO removerpeca-------------------------------
def removerpeca():
    print('bem vindo ao menu de remoção de peças')
    entrada = int(input('Digite o código da peça: '))
    for peca in listapecas:
        if(peca['codigo'] == entrada):
            listapecas.remove(peca)
#---------------------FIM removerpeca-----------------------------




#------------------------INICIO PROGRAMA PRINCIPAL-------------------------

print('bem vindo ao menu principal')
codigopeca = 0
while True:
     y = float(input('Digite a opcao desejada:\n 1 - Cadastrar peça\n 2 - Consultar peça\n 3 - Remover peça\n 4 - sair\n>>'))
     if y == 1:
        codigopeca = codigopeca + 1
        cadastrarpeca(codigopeca)
     elif y == 2:
        consultarpeca()
     elif y == 3:
        removerpeca()
     elif y == 4:
        print('Saindo...')
        break
     else:
        print('Opção inválida')

#-------------------------FIM PROGRAMA PRINCIPAL--------------------------
