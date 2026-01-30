import os

restaurantes=[]


def cadastrar_novo_restaurante():
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    main()


def listar_restaurantes():
    for restaurante in restaurantes:
     nome_restaurante = restaurante['nome']
     categoria = restaurante['categoria']
     ativo = restaurante['ativo']
     print(f' - {nome_restaurante} | {categoria} | {ativo}')

    main()
  

def alternar_estado_restaurante():
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

                
    main()


def main():
    os.system("clear")
    
    opcao_escolhida = int(input(
"Escolha uma das opções abaixo: \n" 
"1 - Cadastrar restaurante\n" 
"2 - Listar restaurantes\n" 
"3 - Ativar restaurante\n"
"4 - Sair do sistema\n"))
    if opcao_escolhida == 1: 
      print('Cadastrar restaurante')
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2: 
      print('Listar restaurantes')
      listar_restaurantes()
    elif opcao_escolhida == 3: 
      print('Ativar restaurante')
      alternar_estado_restaurante()
    elif opcao_escolhida == 4: 
      finalizar_app()
    else:
      finalizar_app()

main()





