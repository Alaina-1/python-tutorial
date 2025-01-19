
income = float(input("Enter your annual income: ₹"))
tax = 0

if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = (income- 600000) *0.10 + 15000
elif income <= 1200000:
    tax = (income -900000) *0.15 + 45000
elif income <= 1500000:
    tax = (income - 1200000) *0.20 + 90000
else:
    tax = (income - 1500000) *0.30 + 150000

print(" total tax " ,tax)
 