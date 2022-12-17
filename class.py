# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def info (self):
#         pass
#         print(self.name,self.rollno)

# student1=student("Pushp","50")
# student2=student("Rishav","35")
# student1.info()
# student2.info()

# class person:
#     def __init__(self):
#         self.name="ishan"
#         self.number=32
#     def compare(self,other):
#         if self.number==other.number:
#             return True
#         else:
#             return False
# p1=person()
# p2=person()
# print(p2.compare(p1))
# # p1.name="kishan"
# # print(p1.name)
# # print(p2.name)
# class car:
#     def __init__(self):
#         self.company="BMW"
#         self.mileage=10
# car1=car()
# car2=car()
# car.wheels=5
# print(car1.mileage,car1.wheels)
# print(car2.mileage,car2.wheels)
# class student:
#     collegename="LPU"
#     def __init__(self,python,web,math):
#         self.subject1=python
#         self.subject2=web
#         self.subject3=math
#     def avg(self):
#         return((self.subject1+self.subject2+self.subject3)/3)
# # this is a class method
#     @classmethod
#     def collegedetail(cls):
#         return cls.collegename
# student1=student(4,7,8)
# student2=student(2,3,9)
# print(student1.avg())
# print(student.collegedetail())
# class A:
#     def __init__(self):
#         print("init of class A")
#     def method1(self):
#         print("This is method 1")
#     def method2(self):
#         print("this is method 2")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("init of class b")
#     def method3(self):
#         print("this is method 3")
#     def method4(self):
#         print("this is method 4")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("init of class c")
#     def method5(self):
#         print("this is method 5")
# obj=C()
# obj.method3()
class Bird:
    def wings(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
    
class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can not fly")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.eyes()
bird.wings()
bird.fly()
ostrich.fly()