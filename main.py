import os
from colorama import Fore

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
            try:
                inteiro = int(input('Insira um número inteiro entre 1 e 3999: '))
                if inteiro <= 3999:
                    mostrar = verificar(inteiro)
                    print('\nO número ' + Fore.GREEN + str(inteiro) + Fore.RESET + ' em  romano é: ' + Fore.GREEN + mostrar + Fore.RESET)
                    inteiro = new_verification(inteiro)
                else:
                    print(Fore.RED + 'Número inválido' + Fore.RESET)
                    inteiro = 0
            except ValueError:
                print(Fore.RED + 'Digite um valor valido!' + Fore.RESET)
                os.system('pause')
                os.system('cls') or None
                inteiro = 0

def new_verification(inteiro):
    x = True
    while x:
        try:
            novamente = int(input('\nGostaria de verificar outro numero?\n\n(1) Sim (2) Não\n\nDigite sua opção: '))
            if novamente == 1:
                os.system('cls') or None

                inteiro = 0
                x = False
                return inteiro

            else:
                os.system('cls') or None
                print('Obrigado!')
                inteiro = 4000
                x = False
                return inteiro
                    
        except ValueError:
            print(Fore.RED + 'Digite um valor valido!' + Fore.RESET)
         
if __name__ == '__main__':
    mostrar()
