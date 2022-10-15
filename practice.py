import random
print(random.randrange(0,1000))


years_spent=int(input("how many years have you spent:"))
salary=int(input("what's you current salary:"))
if years_spent>10 :
    print("your total bonus is:", salary+(salary*0.1))
elif years_spent>6 and years_spent<10:
    print("your total bonus is:",salary+(salary*0.08))
elif years_spent<6:
    print("your total bonus is:",salary+(salary*0.05))
else:
    print("bonus not applicable")