# calculating profit or loss of investment

print("\n\t\t\tInvestment Report")
print("-" * 70)

total_invested = 0
total_current = 0

num = int(input("How many investments? "))
for _ in range(num):
    name = input("\nInvestment name: ")
    invested = float(input("Amount invested: "))
    current = float(input("Current value: "))
    profit_loss = current - invested
    total_invested += invested
    total_current += current
    print("\nName\tInvested\tCurrent Value\tProfit/Loss")
    print(f"{name}\t{invested}\t\t{current}\t\t{profit_loss}")
    if profit_loss < 0:
        print("\t\t\t\t\tLoss")
    elif profit_loss > 0:
         print("\t\t\t\t\tProfit")
    else:
        print("\t\t\t\t\tNo profit or loss")

total_profit_loss = total_current - total_invested
print("-" * 70)
print(f"Total\t{total_invested}\t\t{total_current}\t\t{total_profit_loss}")
if total_profit_loss < 0:
    print("\t\t\t\t\t  Loss")
elif total_profit_loss > 0:
    print("\t\t\t\t\t  Profit")
else:
    print("\t\t\t\t\tNo profit or loss")