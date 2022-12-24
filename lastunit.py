# f = open("demo.txt","r")
# # print(f.read())
# # print(f.readline())
# # print(f.readline())

# f1 = open("demo1.txt", "w")
# f1.write("This is a new file\n")
# f1.write("This is a random text\n")

# for i in f:
#     f1.write(i)


# try:
#     f = open("demo.txt")
    #your code goes here
# finally:
#     f.close()
#This way we are making sure that file is closed properly even if exception is raised that cause the program flow to stop


# with open("demo.txt") as f:
#     f.read() #--> example
#     #your code goes here

# f = open("demo.txt", "r")
# print(f.read(10))
# print(f.tell())



# f = open("img.png", "rb")

# f1 = open("img_copy.png", "wb")

# # print(f.read())

# for i in f:
#     f1.write(i)


# import os

# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("File does not exist")
#try:
    #this block of code will run and throw errors if there are any

#ecxcept:
    #this will raise the errors

#relse:
    #this will execute if there are no errors

#finally
    #this will execute regardless the result of try and except
# try:
#     f=open("list.py")
#     try:
#         f.write("Abc")
#     except:
#         print("Error in file")
#     finally:
#         f.close()
# except:
#     print("Can't open file")
a=5
if a<10:
    raise Exception("Value is less than 5")