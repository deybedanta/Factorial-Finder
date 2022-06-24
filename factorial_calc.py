# Factorial! Calculator

def fact(n):

    f = 1

    for i in range(1,n+1):
        f = f*i

    return f

print("Enter the 'x' in the expression 'x!'.")
x = int(input("> "))

res = fact(x)

print(x,"! (factorial) is equal to",res)
