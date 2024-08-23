# ques: capitalize the first letter of a string
# title="L hV"
# x=title.split()
# y=len(x)
# for i in range(0,y):
#     if len(x[i])>=3:
#         x[i]=x[i].capitalize()
#     else:
#         x[i].lower()
# print(x)
# print(" ".join(x))



#ques: 3069. Distribute Elements Into Two Arrays 
# nums=[2,1,3]
# arr1=[]
# arr2=[]
# arr1.append(nums[0])
# arr2.append(nums[1])
# for i in range(2,len(nums)):
#     if arr1[-1]>arr2[-1]:
#         arr1.append(nums[i])
#     else:
#         arr2.append(nums[i])
# print(arr1+arr2)



#insertion and deletion
# arr=[1,2,3,4,5,6,7,8,9,10]
# arr.insert(2,100)
# print(arr)
# b=2
# a=len(arr)
# while(a!=b):
#     arr[a]=arr[a-1]
#     a=a-1
# print(arr)



# 1374. Generate a String With Characters That Have Odd Counts
# n=4
# if n%2==0:
#     print("a"*(n-1)+"b")
# else:
#     print("a"*n)


#564. Find the Closest Palindrome
# a="1234"
# n=len(a)
# m= n+1//2
# print(m)



# #armstrong numbers
# n=153
# temp=n
# x=len(str(n))
# print(x)
# res=0
# while(n>0):
#     a=n%10
#     n=n//10
#     res=res+(a**x)
# if(temp==res):
#     print("yes")
# else:
#     print("false")



#73 set matrices zero
# x=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# m,n=len(x), len(x[0])
# row,column=[1]*m,[1]*n
# # for getting a flag 
# for i in range(m):
#     for j in range(n):
#         if x[i][j]==0:
#             row[i]=0
#             column[j]=0
# # for row
# for i in range(m):
#     if row[i]==0:
#         x[i]=[0]*n
# for i in range(n):
#     if column[i]==0:
#         for j in range(m):
#             x[j][i]=0
# print(x)



#0118 pascals triangle
# n = 5
# matrix = [[1] * (i + 1) for i in range(n)]

# for i in range(2, n):
#     for j in range(1, i):
#         matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

# print(matrix)



#prime numner brute force
# n=int(input())
# flag=True
# if (n<=1):
#     flag=False

# for i in range(2,n):
#     if n%i==0:
#         flag=False
# print(flag)

#prime number efficient
# root=int(n**(1/2))
# for i in range(2,root):
#     if n%i==0:
#         flag=False
# print(flag)



#prime numbers more optimized
# def isprime(n):
#     if n<=1:
#         return False
#     if n<=3:
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     for i in range(5,int(n**(1/2)),6):
#         if n%i==0 or n%(i+2)==0:
#             return False
#     return True


# n=int(input("Enter the number to be checked:"))
# print(isprime(n))

#fernat's little theorem
# def fernat(p,a):
#     for i in range(2,int(p**(1/2))):
#         if p%i==0:
#             return "P is not a prime number"
#     if p%a==0:
#         return "p is divisible by a"
#     if ((a**(p-1))%p==1):
#         return True
#     return False
# p=int(input("enter the value of p:"))
# a=int(input("enter the value of a:"))
# print(fernat(p,a))


