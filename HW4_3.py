import sys
n = int(input("Enter a number: "))  #amount of stairs
step = 0            #current step
ways = 1          #amount of ways

sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(10**6)

def count(n,step, ways):
    try:
        if n == 0:
            return 0
        elif n-step>1:
            return (count(n,step+1, ways) + count(n,step+2, ways))
        else:
            return ways
    except RecursionError:
        print("RecursionError, reduce the number")


print(count(n, step, ways))

