#for i in a:
#    print(i)
#
#for i in range(0,10,2):
#    print(i)

#classes=["koc26","koc27","koc28"]
#student=["pushp","prateek","utkarsh"]
#for i in student:
#    for j in classes:
#        print(i,j)
#a=int(input())
#for i in range(1,a):
#    a+=i
#print(a)
import sys
print(sys.getrecursionlimit)
sys.setrecursionlimit(2000)
def hello():
    print("hello world")
    hello()
hello()
def hello_mars():
    print("Hello mars")
hello_mars()
def name(x):
    print("hello",x)
x=str(input())
name(x)
def multiply(x,y):
    a=x*y
    return a
b=multiply(2,5)
print(b)