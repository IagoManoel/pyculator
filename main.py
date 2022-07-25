#simple_calculator made by Iago Manoel

#Menu:
print("______________________________")
print("|         PY_CULATOR          |")
print("|_____________________________|")
print("|  version: 0.2               |")
print("|  made by: Iago Manoel       |")
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
    
    #number questions:
    p = input('qual operação você quer usar? ')
    n1 = int(input('qual o primeiro número? (da esquerda) '))
    n2 = int(input('qual o segundo? (da direita '))
    print(" ")
    
    #maths:
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
        
#run the code again:
code()
while True:
    again = input("quer fazer outra conta? [Y/N] ")
    if again == "y":
        code()