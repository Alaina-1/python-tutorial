# calcilating profit or less of investment

print("\n\tInvestment Report")
print("\n3Name\tInvested\tCurrent Value\tProfit/Loss")
print("-" * 40)

total_invested = 0
total_current = 0

num = int(input("How many investments? "))
for _ in range(num):
    name = input("Investment name: ")
    invested = float(input("Amount invested: "))
    current = float(input("Current value: "))
    profit_loss = current - invested
    if profit_loss < 0:
        print("Loss")
    else:
        print("Profit")

    total_invested += invested
    total_current += current
    print(f"{name}\t{invested}\t{current}\t{profit_loss}")
if profit_loss < 0:
        print("Loss")
else:
        print("Profit")

total_profit_loss = total_current - total_invested
print("-" * 40)
print(f"Total\t{total_invested}\t{total_current}\t{total_profit_loss}")
