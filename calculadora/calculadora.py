#passo 1
# criar a função
#criar o menu

#passo 2
# pedir pro usuario escolher uma das opções

#passo 3
#colocar um loop

def calculadora():
   while True: 
    print('Bem Vindo a Calculadora Simples\n')
    print('1. Soma')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisão')
    print('s. Sair')
    
    conta = input('escolha uma opção ou pressione s para sair: ')

    if conta == 's' or conta == 'S':
        print('Obrigado por usar a calculadora simples')
        break
    
    if conta not in ['1','2','3','4']:
       print('essa opção não é válida. Tente novamente.')
       continue

    numero_1 = float(input('digite um número para fazer uma operação: '))
    numero_2 = float(input('digite outro número: '))


    if conta == '1':
       resultado = numero_1 + numero_2
       print(f'A soma de {numero_1} mais o numero {numero_2} é: {resultado}') 
    elif conta == '2':
       resultado = numero_1 - numero_2
       print(f'A subtração de {numero_1} menos o numero {numero_2} é: {resultado}') 
    elif conta == '3':
       resultado = numero_1 * numero_2
       print(f'A multiplicação de {numero_1} multiplicado pelo numero {numero_2} é: {resultado}') 
    else:
       if numero_2 == 0:
          print('A divisão por 0 não é possível')
       else:
          conta == '4'
          resultado = numero_1 / numero_2
          print(f'o resultado de {numero_1} dividido por {numero_2} é: {resultado}')
          


calculadora()
              
      
  
     

