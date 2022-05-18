#_________calculadora simples criada para treinamento_____________

oper = input('qual operação você quer usar? ')

if oper == 'adicao':
    n1 = int(input('digite um número: '))
    n2 = int(input('digite outro número: '))
    s = n1 + n2
    print('a soma entre {} e {} vale {}'.format(n1,n2,s))
 
if oper == 'subtracao':
    n1 = int(input('digite um número: '))
    n2 = int(input('digite outro número: '))
    s = n1 - n2
    print('a subtracão entre {} e {} vale {}'.format(n1,n2,s))

if oper == 'multiplicacao':
    n1 = int(input('digite um número: '))
    n2 = int(input('digite outro número: '))
    s = n1 * n2
    print('o resultado é', s)

if oper == 'divisao':
    n1 = int(input('digite um número: '))
    n2 = int(input('digite outro número: '))
    s = n1 / n2
    print('o resultado é', s)
