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
a="1234"
n=len(a)
m= n+1//2
print(m)