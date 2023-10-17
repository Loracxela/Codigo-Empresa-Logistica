# ---------------Inicio da função dimensão()---------------
total = 0
def dimensão():  # Para a criação de uma função

    print('----------dimensão - 1000 de 100000 --------- :')
    while True: # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
        try: # try permite lidar com erros e exceções que podem ocorrer durante a execução
          altura = float(input('Digitar a altura do objecto em cm:')) # Solicita da altura do objeto
          comprimento = float(input('Digitar a comprimento do objecto em cm:')) # Solicita da cumprimento do objeto
          largura = float(input('Digitar a largura do objecto em cm:')) # Solicita da largura do objeto
        except ValueError:
            print('Valor incorreto. Digite um valor númerico.') # Mostra quando erra o valor númerico
            continue
        dimensão = altura * largura * comprimento
        print('A dimensão do objeto é:' , dimensão,'(cm)' )

        if dimensão < 1000:    # Funsão if significa 'se', ela é execultada apenas se a condição for verdadeira
           return 10    # Declara a informação a ser retornada pela função
        elif dimensão <= 1000 and dimensão < 10000:  # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
           return 20
        elif dimensão <= 10000 and dimensão < 30000:
           return 30
        elif dimensão <= 30000 and dimensão < 100000:
           return 50

        else:  # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso
                print('Pare de digitar dimensões que não existem:')
                continue


        # Fim da função dimensões()


# Inicio da função peso()
def peso():  # Para a criação de uma função
    print('----------peso - 1 de 3 --------- :')
    while True: # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
        try:
           peso = float(input('Digite o peso do objeto (em Kg):' ))

           if peso <= 0.1:  # Funsão if significa 'se', ela é execultada apenas se a condição for verdadeira
              return 1   # Declara a informação a ser retornada pela função
           elif peso <= 0.1 and peso < 1 : # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
              return 1.5
           elif peso <= 1 and peso < 10:
              return 2
           elif peso <= 10 and peso < 30:
              return 3

           else:     # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso
             print('Não aceitamos objetos tão pessados: ')
             continue
        except ValueError:
         print('Digite somente valores númericos:' )

# Fim da função peso_obj ()

# Inicio da função rota ()
def rota():  # Para a criação de uma função
    print('----------rota - 6 de 6 --------- :')
    while True: # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
        rota = input('\nDigita alguma rota: \n' +  # Input permite solicitar uma informação ao usuário, faz um login em um sistema
                     'RS - De Rio de Janeiro até São Paulo \n' +
                     'SR - De São Paulo até Rio de Janeiro \n' +
                     'BS - De Brasília até São Paulo \n' +
                     'SB - De São Paulo até Brasília \n' +
                     'BR - De Brasília até Rio de Janeiro \n' +
                     'RB - Rio de Janeiro até Brasília \n' +
                     '>>')

        if rota == 'RS': # Funsão if significa 'se', ela é execultada apenas se a condição for verdadeira
            return 1  # Declara a informação a ser retornada pela função
        elif rota == 'SR': # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'SB':
            return 1.2
        elif rota == 'BR':
            return 1.5
        elif rota == 'RB':
            return 1.5
        else:  # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso
            print('Rota invalida, por favor tente novamente')

        print('Rota invalida, por favor tente novamente!')


# Fim da função rota ()

# Inicio do Main
print('----------Bem-vindo (a) empresa de logística --------- :')
dimensão = dimensão()
peso = peso()
rota = rota()
total = dimensão * peso * rota

print('O total a pagar: R${:.2f} dimensão{} peso{} rota{}'.format(total, dimensão, peso, rota))