import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, atualmente eu tenho 21 anos {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, eu sou estudando de Gestao da tecnologia da informação (GST){os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Sim estudo muito pra isso kkk{os.linesep}')
    else:
        print('Digite apenas 1,2, ou 3')

def start():
    #aprensentar o chatbot
    print('Olá Bem vindo ao Chatbot do Nicolas')
    #pedir o nome
    nome = input('Digite seu nome: ')
    #pedir o email
    email = input('Digite seu email: ')
    while True:
    #Oferecer o menu de opções
        resposta = input(
        f'O que gostaria de saber hoje?{os.linesep}[1] - Quantos anos?{os.linesep}[2] - O que vc faz da vida?{os.linesep}[3] - Pretende sair do pais?{os.linesep}')
    #Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
