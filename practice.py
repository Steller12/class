#question number 2
a=5
for rows in range(a,0,-1):
    for column in range(rows,0,-1):
        print(column,end='')
    print("")

#question number 1
for rows in range(1,a+1):
    for column in range(1,rows+1):
        print(column,end='')
    print("")

#question number 3
min = int(input("min"))
max = int(input("max"))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)

#question number 4
b = [0, 1]
N = 10
c = 3
while c < N + 1:
    value = b[c - 2] + b[c - 3]
    b.append(value)
    c = c + 1
print(b)

#question 5
A=int(input("number"))
C=[]
for i in range(0,A):
    B=str(input("string"))
    if "Dr." in B:
        C.append(B)
print(C)

#question 6
