def dimensoesObjeto():
    while True:
        try:
            altura = float(input('Digite a altura do objeto (em cm): ' ))
            if altura <= 0:
                print('A altura precisa ser um número positivo.\nComece novamente')
                continue
            comprimento = float(input('Digite o comprimento do objeto (em cm): ' ))
            if comprimento <= 0:
                print('O comprimento precisa ser um número positivo.\nComece novamente')
                continue
            largura = float(input('Digite a largura do objeto (em cm): ' ))
            if largura <= 0:
                print('A largura precisa ser um número positivo.\nComece novamente')
                continue
            volume = altura * largura * comprimento
            if volume:
                valor = 0
                print('O volume do objeto é (em cm³): {}'.format(volume))
                if 0 < volume < 1000:
                    valor = 10
                elif 1000 < volume < 10000:
                    valor = 20
                elif 10000 < volume < 30000:
                    valor = 30
                elif 30000 < volume < 100000:
                    valor = 50
                elif volume > 100000:
                    print('Não aceitamos objetos com dimensões tão grandes\nEntre com as dimensões desejadas novamente')
                    continue
                return valor
        except:
            print('Você digitou alguma dimensão do objeto com valor não numérico\nPor favor entre com as dimensões desejadas novamente')
            continue
def pesoObjeto():
    while True:
        try:
            multiplicador = 1
            peso = float(input('Digite o peso do objeto (em kg): '))
            if peso <= 0:
                print('O peso precisa ser um número positivo.\nDigite novamente um peso válido')
                continue
            if 0.1 <= peso < 1:
                multiplicador = 1.5
            elif 1 <= peso < 10:
                multiplicador = 2
            elif 10 <= peso < 30:
                multiplicador = 3
            elif peso >= 30:
                print('Não aceitamos objetos tão pesados\nEntre com o peso desejado novamente')
                continue
            return multiplicador
        except:
            print('Você digitou peso do objeto com valor não numérico\nPor favor entre com o peso desejado novamente')
            continue
def rotaObjeto():
    rotas = {
        RS: {percurso: 'De Rio de Janeiro até São Paulo', multiplicador: 1},
        SR: {percurso: 'De São Paulo até Rio de Janeiro', multiplicador: 1}
    }
    print('Selecione a rota:')
    print(' BR - De Brasília para Rio de Janeiro')
    print(' BS - De Brasília para São Paulo')
    print(' RB - De Rio de Janeiro para Brasília')
print('Bem Vindo a Companhia de Logística Yuri Lopes Maria')
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

