import json
import time
from tqdm import tqdm

def ler_banco():
    '''FUNÇÃO QUE LÊ O BANCO DE DADOS'''
    with open('banco_de_dados.json','r') as pacientes:
        return json.load(pacientes)

def salvar(Banco_pacientes):
    '''FUNÇÃO QUE GRAVA OS PACIENTES CADASTRADOS NO BANCO DE DADOS'''
    try:
        with open('banco_de_dados.json','w') as pacientes:
            pacientes.write(json.dumps(Banco_pacientes, indent=4))
    except :
        print('Erro ao salvar dados no banco.')
    else:
        print('Paciente cadastrado com sucesso! ')


def adicionar_paciente():
    '''FUNÇÃO QUE ADCIONA PACIENTES AO BANCO DE DADOS'''
    
    nome = str(input('Digite o nome do(a) Paciente: '))
    idade = int(input('Digite o idade do(a) Paciente: '))
    peso = float(input('Digite o peso do(a) Paciente: '))
    bf = float(input('Digite o bf do(a) Paciente: '))
    objetivo = str(input('Digite o objetivo do(a) Paciente: '))
    
   
    Banco_pacientes = ler_banco()
    Banco_pacientes['Nome'].append(nome)
    Banco_pacientes['Idade'].append(idade)
    Banco_pacientes['Peso'].append(peso)
    Banco_pacientes['BF'].append(bf)
    Banco_pacientes['Objetivo'].append(objetivo)
    salvar(Banco_pacientes)


def listar_pacientes():
    '''FUNÇÃO QUE MOSTRA A LISTA DE PACIENTES CADASTRADOS'''
    Banco_pacientes = ler_banco()
    qtd_linhas = len(Banco_pacientes['Nome'])
    print('LENDO ARQUIVO...\n')
    
    for i in tqdm(range(3), colour='MAGENTA'):
        time.sleep(1)
        
    for linha in range(qtd_linhas):
        print(f'\n\nPACIENTE: {Banco_pacientes["Nome"][linha]}')
        print(f'IDADE: {Banco_pacientes["Idade"][linha]}')
        print(f'PESO: {Banco_pacientes["Peso"][linha]}')
        print(f'BF: {Banco_pacientes["BF"][linha]}')
        print(f'OBJETIVO: {Banco_pacientes["Objetivo"][linha]}')
        



    
