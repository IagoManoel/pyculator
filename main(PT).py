#calculadora simples feita por Iago Manoel
#essa é a versão em português da calculadora, feita para o público brasileiro, o outti arquivo(main.py) está em inglês.

#Menu:
print("______________________________")
print("|         PY_CULATOR          |")
print("|_____________________________|")
print("|  versão: 0.2                |")
print("|  feito por: Iago Manoel     |")
print("|                             |")
print("|  operações disponiveis:     |")
print("|  a: adição                  |")
print("|  s: subtração               |")
print("|  m: multiplicação           |")
print("|  d: divisão                 |")
print("|  p: potência                |")
print("|_____________________________|")
print("")
    
def code():
    print("  ")
    print("   ")
    
    #perguntas sobre os números:
    p = input('qual operação você quer usar? ')
    n1 = int(input('qual o primeiro número? (da esquerda) '))
    n2 = int(input('qual o segundo? (da direita '))
    print(" ")
    
    #estrutura principal:
    if p == "a":
        print("conta: ",n1, "+", n2)
        print("resultado: ", n1 + n2)
    if p == "s":
        print("conta: ",n1, "-", n2)
        print("resultado: ", n1 - n2)
    if p == "m":
        print("conta: ",n1, "x", n2)
        print("resultado: ", n1 * n2)
    if p == "d":
        print("conta: ",n1, "÷", n2)
        print("resultado:", n1 / n2)
    if p == "p":
        print("conta: ",n1, "^", n2)
        print("resultado: ", n1 ** n2)
        
#rodar o código de novo?:
    again = input("quer fazer outra conta? [Y/N] ")
    if again == "y":
        code()
        
code()