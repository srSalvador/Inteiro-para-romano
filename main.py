import os

os.system('cls') or None

def verificar(romano):
    dic = {
      1    : 'I',
      4    : 'IV',
      5    : 'V',
      9    : 'IX',
      10   : 'X',
      40   : 'XL',
      50   : 'L',
      90   : 'XC',
      100  : 'C',
      400  : 'CD',
      500  : 'D',
      900  : 'CM',
      1000 : 'M'
    }

    result = ''

    for x in sorted(dic.keys(), reverse=True):
        while romano >= x:
            result += dic[x]
            romano -= x
    return result

def mostrar():
        inteiro = 0
        while inteiro <= 3999:
            inteiro = int(input('Insira um número inteiro: '))
            if inteiro <= 3999:
                mostrar = verificar(inteiro)
                print(f'O número {inteiro} em  romano é: {mostrar}')
                inteiro = new_verification(inteiro)
            else:
                print('Número inválido')
                continue

def new_verification(inteiro):
    novamente = int(input('\nGostaria de verificar outro numero?\n (1) Sim (2) Não\nDigite sua opção: '))
    if novamente == 1:
        os.system('cls') or None
        inteiro = 0
        return inteiro 

    else:
        os.system('cls')
        print('Obrigado!')
        inteiro = 4000
        return inteiro

if __name__ == '__main__':
    mostrar()
