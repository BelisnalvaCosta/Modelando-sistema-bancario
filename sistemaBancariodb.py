# biblioteca MySQL
import pymysql
import random
import getpass

# conectando ao banco de dados
conexão= pymysql.connect(
    host='localhost',
    user = 'root',
    password = '',
    database = 'BD_Bank'
)

cursor = conexão.cursor()

#Realizando Saque da conta
def sacar(self,conta,cpf):
    user_list =[]
    cursor.execute(f'select Saldo from Users where Senha = {self} AND CPF ={cpf}')
    for x in cursor:
        user_list.append(x)
    if user_list.__len__()== 1:
        saldo = str(user_list)
        saldo = float(saldo[1:-2])
        valor = float(input('digite o valor para saque'))
        if (saldo-valor) < 0:
            print('saldo insulficiente')
        else:
            saldo = (saldo-valor)
            cursor.execute(f'UPDATE Users SET Saldo = {saldo} WHERE CPF ={cpf}')
            conexão.commit()
            print('saque efetuado com sucesso')
    else:
        print('conta ou senha incorreta \n verifique os dados e tente novamente')

# Criando Usuario
def criar_usuario(self, cpf, rg, senha, agencia , saldo):

    conta = random.randint(100000, 999999)
    cursor.execute(f'insert into Users (Nome, CPF, RG, Conta, Agencia, Senha, Saldo ) VALUES({self}, {cpf}, {rg}, {conta}, {agencia}, {senha}, {saldo}) ')
    print(f'sua conta é {conta} e sua agencia é {agencia}')

def depositar(self, cpf, conta, conta2,cpf2, valor):
    cursor.execute(f'SELECT Saldo FROM Users WHERE Senha = {self} AND Conta = conta')
    for x in cursor:
        saldo = str(x)
        saldo = float(saldo[1:-2])

    if (saldo - valor) >= 0:
        cursor.execute(f'UPDATE Users set Saldo = {saldo - valor} WHERE CPF = {cpf} AND Conta = {conta}')
        cursor.execute(f'UPDATE Users set Saldo = Saldo + {valor} WHERE CPF = {cpf2} AND Conta = {conta2}')
        print('trasferencia realizada com sucesso')

def exibir_saldo():

def exibir_extrato():

def main():