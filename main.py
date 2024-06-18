import Funcoes
import os

os.system('cls')
print('=======BEM VINDO!!=======\n***** NUTRIFELA *****\n')


escolha = {
   '1': Funcoes.adicionar_paciente,
   '2': Funcoes.listar_pacientes,
}

while True:
    print('\n\nDIGITE O NÚMERO CORRESPONDENTE A UMA OPÇÃO ABAIXO: ')
    print('1 - CADASTRAR PACIENTES')
    print('2 - LISTAR PACIENTES')
    print('3 - SAIR')
    opcao = input('-> ')
    if opcao == '3':
        exit()
    elif opcao not in ['1','2','3',]:
        print('\nDigite uma opção válida!')
    else:
        escolha[opcao]()