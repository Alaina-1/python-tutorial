# calculating loss or profit on investments
def generate_report(investments):
    print("Investment Report")
    print("Name\t      Invested\tCurrent Value\tProfit/Loss |")
    print("-" * 50)
    for name, invested, current in investments:
        profit_loss = current - invested
        print(f"{name}\t{invested}\t   {current}\t\t  {profit_loss}")

# dummy data
investments = [
    ("Stock A      ", 1000  ,  1200),
    ("Stock B      ", 1500  ,  1300),
    ("Mutual Fund C", 2000  ,  2500)
]

generate_report(investments)