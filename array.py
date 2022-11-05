import sys
def sumrec(num):
    if  num==1 :
        return num 
    return num * sumrec(num-1)
ans=sumrec(5)
print(ans)