import sys
sys.setrecursionlimit(10**6)
numb  = [1,1]
def ask():
    global numb
    try:
        numb = []
        numb.append(int(input("Enter the first number: ")))
        numb.append(int(input("Enter the second number: ")))
    except:
        ask()
                                                            #Exit if one of  the numbers is 0
def euclid(numb = []):
    numb.sort()                                             #The biggest number is second
    if numb[0] == 0:
        return numb[1]
    numb[1] -= numb[0]
    return euclid(numb)


ask()
print(euclid(numb))
