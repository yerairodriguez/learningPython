sale1 = int(input("Introduce sales 1: "))
sale2 = int(input("Introduce sales 2: "))
sale3 = int(input("Introduce sales 3: "))

baseSalary = int(input("Introduce base salary"))

total = sale1 + sale2 + sale3

saleComission = total* 10 /100

totalSalary = baseSalary + saleComission


print("This month comissions sales were: %i and total salary was %i" %(saleComission, totalSalary))