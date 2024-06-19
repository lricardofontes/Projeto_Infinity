import json
import time
from tqdm import tqdm

def ler_banco():
    '''FUNÇÃO QUE LÊ O BANCO DE DADOS'''
    with open('banco_de_dados.json','r') as pacientes:
        return json.load(pacientes)

def salvar(Banco_pacientes, operacao='cadastrar'):
    '''FUNÇÃO QUE GRAVA OS PACIENTES CADASTRADOS NO BANCO DE DADOS'''
    try:
        with open('banco_de_dados.json','w') as pacientes:
            pacientes.write(json.dumps(Banco_pacientes, indent=4))
    except :
        print('Erro ao salvar dados no banco.')
    else:
        if operacao == 'cadastrar':
            print('Paciente cadastrado com sucesso! ')
        elif operacao == 'excluir':
            print('Paciente excluído com sucesso!')


def calcular_imc(peso, altura):
    '''FUNÇÃO QUE CALCULA O IMC DO PACIENTE'''
    imc = peso / (altura ** 2)
    return round(imc, 2)  # Arredonda o IMC para duas casas decimais

def adicionar_paciente():
    '''FUNÇÃO QUE ADCIONA PACIENTES AO BANCO DE DADOS'''
    
    nome = str(input('Digite o nome do(a) Paciente: '))
    idade = int(input('Digite a idade do(a) Paciente: '))
    peso = float(input('Digite o peso do(a) Paciente (em kg): '))
    altura = float(input('Digite a altura do(a) Paciente (em metros): '))
    bf = float(input('Digite o bf do(a) Paciente: '))
    objetivo = str(input('Digite o objetivo do(a) Paciente: '))
    
    imc = calcular_imc(peso, altura)
   
    Banco_pacientes = ler_banco()
    Banco_pacientes['Nome'].append(nome)
    Banco_pacientes['Idade'].append(idade)
    Banco_pacientes['Peso'].append(peso)
    Banco_pacientes['Altura'].append(altura)
    Banco_pacientes['BF'].append(bf)
    Banco_pacientes['Objetivo'].append(objetivo)
    Banco_pacientes['IMC'].append(imc)
    
    salvar(Banco_pacientes)

# Continue com as funções 'listar_pacientes' e 'excluir_paciente' e certifique-se de que elas também lidam com os novos campos 'Altura' e 'IMC'.


def listar_pacientes():
    '''FUNÇÃO QUE MOSTRA A LISTA DE PACIENTES CADASTRADOS'''
    Banco_pacientes = ler_banco()
    qtd_linhas = len(Banco_pacientes['Nome'])
    print('LENDO ARQUIVO...\n')
    
    for i in tqdm(range(3), colour='MAGENTA'):
        time.sleep(1)
        
    for i in range(qtd_linhas):
        print(f'{i+1}. {Banco_pacientes["Nome"][i]} - {Banco_pacientes["Idade"][i]} anos - {Banco_pacientes["Peso"][i]} kg - {Banco_pacientes["Altura"][i]} m - IMC: {Banco_pacientes["IMC"][i]}% - BF: {Banco_pacientes["BF"][i]}% - Objetivo: {Banco_pacientes["Objetivo"][i]}')

        
def excluir_paciente():
    '''FUNÇÃO QUE EXCLUI UM PACIENTE DO BANCO DE DADOS'''
    Banco_pacientes = ler_banco()
    qtd_linhas = len(Banco_pacientes['Nome'])
    
    # Listar os pacientes
    print('LISTA DE PACIENTES:\n')
    for i in range(qtd_linhas):
        print(f'{i+1}. {Banco_pacientes["Nome"][i]} - {Banco_pacientes["Idade"][i]} anos - {Banco_pacientes["Peso"][i]} kg - {Banco_pacientes["Altura"][i]} m - IMC: {Banco_pacientes["IMC"][i]}% - BF: {Banco_pacientes["BF"][i]}% - Objetivo: {Banco_pacientes["Objetivo"][i]}')
    
    # Solicitar ao usuário que escolha um paciente para excluir
    try:
        escolha = int(input('\nDigite o número do paciente que deseja excluir: ')) - 1
        if 0 <= escolha < qtd_linhas:
            # Excluir os dados do paciente escolhido
            for chave in Banco_pacientes:
                del Banco_pacientes[chave][escolha]
            salvar(Banco_pacientes, operacao='excluir')
            
        else:
            print('Número inválido. Por favor, escolha um número da lista.')
    except ValueError:
        print('Por favor, digite um número válido.')



    
