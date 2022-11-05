def isRectangle(a, b, c, d):
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        return True
    else:
        return False
# Driver code
a= int(input())
b= int(input())
c=int(input())
d=int(input())
if isRectangle(a,b,c,d):
    print("possible")
else:
    print("not possible")