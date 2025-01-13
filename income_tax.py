income = float(input("Enter your income: "))
if income <= 25000:
    tax = 0
elif income <= 50000:
    tax = 0.05 * (income - 25000)
elif income <= 100000:
    tax = 1250 + 0.1 * (income - 50000)  # 1250 comes from 0.05 * 25000
elif income <= 150000:
    tax = 6250 + 0.15 * (income - 100000)  # 6250 comes from 1250 + 0.1 * 50000
else:
    tax = 11250 + 0.2 * (income - 150000)  # 11250 comes from 6250 + 0.15 * 50000

print("Income tax: ", tax)
