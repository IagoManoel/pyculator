#simple_calculator made by Iago Manoel

#Menu:
print("   ______________________________")
print("   |         PY_CULATOR          |")
print("   |_____________________________|")
print("   |  version: 0.2               |")
print("   |  made by: Iago Manoel       |")
print("   |                             |")
print("   |  available operations:      |")
print("   |  a: addition                |")
print("   |  s: subtraction             |")
print("   |  m: multiplication          |")
print("   |  d: division                |")
print("   |  p: potentiation            |")
print("   |_____________________________|")
print("")
    
def code():
    print("  ")
    print("   ")
    
    #questions about numbers:
    p = input('which operation do you want to use? ')
    n1 = int(input('whats the first number? (from left)'))
    n2 = int(input('whats the second? (from right)'))
    print(" ")
    
    #Main structure:
    if p == "a":
        print("calculation: ",n1, "+", n2)
        print("result: ", n1 + n2)
    if p == "s":
        print("calculation: ",n1, "-", n2)
        print("result: ", n1 - n2)
    if p == "m":
        print("calculation: ",n1, "x", n2)
        print("result: ", n1 * n2)
    if p == "d":
        print("calculation: ",n1, "÷", n2)
        print("result:", n1 / n2)
    if p == "p":
        print("calculation: ",n1, "^", n2)
        print("result: ", n1 ** n2)
        
#run the code again:
    again = input("want to do another calculation?  [Y/N] ")
    if again == "y":
        code()
        
code()