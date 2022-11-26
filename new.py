#x=lambda num1,num2: num1+num2
#print(x(3,5))
def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
a=int(input("first number: "))
b=int(input("second number: "))
c=str(input("operator: "))
if c=='+':
    sum(a,b)
elif c=='-':
    sub(a,b)
elif c=='*':
    mult(a,b)
else:
    div(a,b)