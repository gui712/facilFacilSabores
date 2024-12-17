import os

restaurantes = [{'nome':'Gato-Veio','categoria':'Pizzaria','ativo':False},
                {'nome':'Prças', 'categoria': 'Japonesa', 'ativo':True},
                {'nome':'Cumida Di Buteco', 'categoria':'Bar','ativo': False}]

def exibir_nome_programa():
    print('Facil Facil Sabores!\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o Programa')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu()

def listar_restaurante():
    exibir_subtitulo('Listando todos restaurantes')
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal:. ')
    main()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante_alterar = input('\nDigite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante_alterar == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante_alterar} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante_alterar} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante não foi encontrado')
    
    voltar_ao_menu()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurante()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

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