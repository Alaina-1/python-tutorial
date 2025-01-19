investment=float(input("investment amount: "))
interest=float(input("annual interest rate: "))
year=int(input("years: "))

print("\nyear\t rate")
print("-------------------")
for y in range(1,year+1):
    si=float(investment*interest)/100
    investment=investment+si
    print( y,"\t" ,round(investment,2))
print("\n")