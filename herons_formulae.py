#for heron's formulae
from math import sqrt

#sides input
first_side=int(input("enter the first side of the triangle:"))
second_side=int(input("enter the second side of the triangle:"))
third_side=int(input("enter the third side of the triangle:"))

#perimeter
perimeter=first_side+second_side+third_side

#semi perimeter
semi_perimeter=int(perimeter/2)

#heron's formulae
area_using_herons=sqrt(semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))
print("the area of the triangle is:",area_using_herons)