import os

restaurantes = []

def exibir_nome_programa():
    print('Facil Facil Sabores!\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o Programa\n')


def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!!')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()