# import statistics

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


# #189. Rotate Array

# def rotate(k,n):
#     while k>0:
#         temp=n[-1]
#         for i in range(len(n)-1):
#             n[i+1]=n[i]
#         n[0]=temp
#         k=k-1
#     return n
# n=[1,2,3,4,5,6,7]
# k=3
# print(rotate(k,n))



#56. merge intervals 
# arr=[[1,3],[2,6],[8,10],[8,9],[9,11],[15,18],[2,4],[16,17]]
# for i in range(0,len(arr)):
#     for j in range(0,len(arr)-i-1):
#         if arr[j][0]>arr[j+1][0]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# for i in range(0,len(arr)-1):
#     if(arr[i][1]>=arr[i+1][0]):
#         a=[arr[i][0],arr[i+1][1]]
#         arr.pop(i+1)
#         arr.append(a)
# print(arr)





#sieve of eratosthenes nloglogn
# def SieveOfEratosthenes(num):
#     prime = [True for i in range(num + 1)]
#     p = 2  

#     while p * p <= num:
#         if prime[p]:
#             for i in range(p * p, num + 1, p):
#                 prime[i] = False
#         p += 1

#     # Print all prime numbers
#     for p in range(2, num + 1):
#         if prime[p]:
#             print(p)

# num = 30
# print(num)
# SieveOfEratosthenes(num)


#segmented sieve





#sieve of atkin







# # #linked list
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class linked_list:
#     def __init__(self):
#         self.head=None
#     # def remove():
#     def traverse(self):
#         if self.head is None:
#             print("empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data,"---->",end=" ")
#                 n=n.ref
#     def insert_begin(self,data):
#         new_node=node(data)
#         new_node.ref=self.head
#         self.head=new_node
#     def insert_end(self,data):
#         new_node = node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node

            

# l=linked_list()
# l.insert_begin(10)
# l.insert_begin(100)
# l.insert_begin(1000)
# l.insert_end(1)
# l.traverse()



# arr=[3,1,4,1,2,100]
# n=len(arr)
# sum=0
# for i in range(0,n):
#     sum=sum+arr[i]
# left=0
# ind=0
# for i in range(0,n):
#     left=left+arr[i]
#     if(left>(sum-left)):
#         ind=i
#         if(sum-left==0):
#             ind=-1
#         break
# print(ind)

# arr=[1,3,4,8]
# queries=[[0,1],[1,2],[0,3],[3,3]]
# ans=[]
# for i in range(0,len(queries)):
#     temp=arr[queries[i][0]]
#     print(temp)
#     for j in range(queries[i][0]+1,queries[i][1]):
#         temp=(temp^arr[j])
#     ans.append(temp)
# print(ans)
# print(1^3)



# import math

# # Function to compute the greatest common divisor
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Function to compute the modular inverse
# def mod_inverse(e, phi):
#     for d in range(1, phi):
#         if (e * d) % phi == 1:
#             return d
#     return None

# # RSA encryption and decryption implementation
# def rsa_decrypt(p, q, e, C):
#     # Step 1: Calculate n = p * q
#     n = p * q
    
#     # Step 2: Calculate φ(n) = (p - 1) * (q - 1)
#     phi = (p - 1) * (q - 1)
    
#     # Step 3: Calculate d as the modular inverse of e under φ(n)
#     d = mod_inverse(e, phi)
    
#     # Step 4: Decrypt the message M = (C^d) % n
#     M = pow(C, d, n)
    
#     return M

# # Example usage
# encrypted_message = int(input())
# e = int(input()) 
# p = int(input())  
# q = int(input()) 


# decrypted_message = rsa_decrypt(p, q, e, encrypted_message)
# print(decrypted_message)






# a=str(input())
# cnt=0
# print(sorted(a))
# for i in range(len(a)):
#     if i==0:
#         if a[i]!=a[i+1]:
#             cnt+=1
#     elif i==len(a)-1:
#         if a[i]!=a[i-1]:
#             cnt+=1
#     elif a[i]!=a[i+1] and a[i]!=a[i-1]:
#         cnt+=1
#     else:
#         continue
# print(cnt)




# arr=[60,14,25,45]
# arr2=[]
# target=int(input())
# for i in range(len(arr)):
#     if arr[i]<50:
#         arr2.append(target)
#         arr2.append(arr[i])
#     else:
#         arr2.append(arr[i])
# print(arr2)


# s=0
# a=[1,4,5,3,2,7,6]
# b=[]
# for i in range(len(a)):
#     s+=a[i]
#     b.append(s)
# print(b)



#given an array of integers and an integer k , return the total number of subarrays whose sum equals to k 
# def subarraySum(nums, k):
#     cum_sum_freq = {0: 1} 

#     total_count = 0
#     cumulative_sum = 0

#     for num in nums:
#         cumulative_sum += num
#         if cumulative_sum - k in cum_sum_freq:
#             total_count += cum_sum_freq[cumulative_sum - k]

#         cum_sum_freq[cumulative_sum] = cum_sum_freq.get(cumulative_sum, 0) + 1

#     return total_count

# my_array = [1, 2, 3, 4, 5]
# target_sum = 9
# result = subarraySum(my_array, target_sum)
# print(f"Total subarrays with sum {target_sum}: {result}")



#inserting an element to the array
# arr=[5,6,7,8,9,4]
# arr.append(3)
# arr.insert(2,4)
# print(arr)



#program to delete an element from the array
# arr.remove(5)
# print(arr)


#program to perform array arrangement
# even=[x for x in arr if x%2==0]
# odd=[x for x in arr if x%2!=0]
# arr= even+odd
# print(arr)




#program to print matrix in a spiral form 
# class stack:
#     def __init__(self) -> None:
#         self.stack=[]
#     def push(self,x):
#         self.stack.append(x)
#     def pop(self):
#         if len(self.stack)!=0:
#             return self.stack.pop()
#         return("pop from empty stack")
#     def peek(self):
#         if len(self.stack)!=0:
#             return self.stack[-1]
#         return("peek from empty stack")


# s=stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.pop())
# print(s.pop())
# print(s.peek())
# print(s.pop())
# print(s.pop())
# print(s.peek())




# def left_most_digit(arr):
#     arr2=[]
#     for i in arr:
#         arr2.append(int(str(i)[0]))
#     arr2.sort(reverse=True)
#     arr2[-1],arr2[-2]=arr2[-2],arr2[-1]
#     ans=0
#     for i in arr2:
#         ans=ans*10+i
#     return ans
# arr=[1,21,321,449,54]
# print(left_most_digit(arr))





# n=100
# prime=[True for i in range(n+1)]
# p=2
# while (p*p<=n):
#     if (prime[p]==True):
#         for i in range(p*p,n+1,p):
#             prime[i]=False
#     p+=1
# for i in range(2,n+1):
#     if prime[i]:
#         print(i)


# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


# def SieveOfEratosthenes(n):
#     prime = [True for i in range(n+1)]
#     p = 2
#     while (p * p <= n):
#         if (prime[p] == True):
#             for i in range(p * p, n+1, p):
#                 prime[i] = False
#         p += 1
#     for p in range(2, n+1):
#         if prime[p]:
#             print(p)


# # Driver code
# if __name__ == '__main__':
#     n = 100
#     print("than or equal to", n)
#     SieveOfEratosthenes(n)





# # Python3 program to print all primes 
# # smaller than n, using segmented sieve 
# import math
# prime = []
# def simpleSieve(limit):
#     mark = [True for i in range(limit + 1)]
#     p = 2
#     while (p * p <= limit):
#         if (mark[p] == True): 
#             for i in range(p * p, limit + 1, p): 
#                 mark[i] = False  
#         p += 1
#     for p in range(2, limit): 
#         if mark[p]:
#             prime.append(p)
#             print(p,end = " ")
# def segmentedSieve(n):
#     limit = int(math.floor(math.sqrt(n)) + 1)
#     simpleSieve(limit)
#     low = limit
#     high = limit * 2
#     while low < n:
#         if high >= n:
#             high = n
#         mark = [True for i in range(limit + 1)]
#         for i in range(len(prime)):
#             loLim = int(math.floor(low / prime[i]) * prime[i])
#             if loLim < low:
#                 loLim += prime[i]
#             for j in range(loLim, high, prime[i]):
#                 mark[j - low] = False
#         for i in range(low, high):
#             if mark[i - low]:
#                 print(i, end = " ")
#         low = low + limit
#         high = high + limit
# n = 100
# print("Primes smaller than", n, ":")
# segmentedSieve(100)



# def insert_min_heap(heap, element):
#     heap.append(element)
#     heapify_up(heap, len(heap) - 1) 

# def heapify_up(heap, index):
#     while index > 0:
#         parent_index = (index - 1) // 2  
#         if heap[index] < heap[parent_index]:
#             heap[index], heap[parent_index] = heap[parent_index], heap[index]
#             index = parent_index  
#         else:
#             break  

# my_heap = [10, 20, 30, 40, 50]

# def build_min_heap(arr):
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1): 
#         heapify_down(arr, n, i)  

# def heapify_down(arr, n, i):  
#     smallest = i  
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and arr[left] < arr[smallest]:
#         smallest = left

#     if right < n and arr[right] < arr[smallest]:
#         smallest = right

#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]

#         heapify_down(arr, n, smallest)

# build_min_heap(my_heap)

# print(f"Original heap: {my_heap}")
# a= int(input())
# insert_min_heap(my_heap, a)
# print(f"Heap after inserting {a}: {my_heap}")





# def heapify(heap, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and heap[left] < heap[smallest]:
#         smallest = left

#     if right < n and heap[right] < heap[smallest]:
#         smallest = right

#     if smallest != i:
#         heap[i], heap[smallest] = heap[smallest], heap[i]
#         heapify(heap, n, smallest)

# heap = [10, 9, 7, 6, 8]
# n = len(heap)
# index = 0

# heapify(heap, n, index)
# print(f"Heap after heapify: {heap}")



# from collections import deque

# class node:
#     def __init__(self, val):
#         self.data=val
#         self.left=None
#         self.right=None
# def issym(root):
#     if root is None:
#         return True
#     q=deque()
#     q.append(root.left)
#     q.append(root.right)
#     while q:
#         n1=q.popleft()
#         n2=q.popleft()
#         if n1 is None and n2 is None:
#             continue
#         if n1 is None or n2 is None or n1!=n2:
#             return False
#         q.append(n1.left)
#         q.append(n2.right)
#         q.append(n1.right)
#         q.append(n2.left)
#     return True
# root = node(1)
# root.left = node(2)
# root.right = node(2)
# root.left.left = node(3)
# root.left.right = node(4)
# root.right.left = node(4)
# root.right.right = node(3)
# print(issym(root))

# def topKFrequent(nums, k):
#     d={}
#     ans=[]
#     for i in nums:
#         if i in d.keys():
#             d[i]+=1
#         else:
#             d[i]=1
    
#     return d


# nums=[1,1,1,2,2,2,2,2,3,3,3,1,3]
# k=2
# print(topKFrequent(nums, k))

# if __name__=="__main__":
#     n=int(input())
#     arr=list(map(int,input().split()))
#     arr.sort()
#     print(arr)
#     print(arr[n//2])



# a=[2,4,6,8]
# print(statistics.median(a))



# a=int(input())
# print(a)




