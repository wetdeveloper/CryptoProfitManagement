from app import *


# reinvestments,totalbalance,totalsaved=profitcalculator(stocks_targets)
# print(f"reinvestments:{reinvestments}")
# reinvestmentsmade=sum([item[4] for item in reinvestments])
# print(f"total Balance:{totalbalance}")
# print(f"reinvestment made money:{reinvestmentsmade}$")
# totalbalance+=sum([item[4] for item in reinvestments])
# print(f"totalsaved:{totalsaved}")
# print(f"total Balance+reinvestment made money+total saved profit:{totalbalance+totalsaved}$")






p=Portfolio(stocks_targets)
print(p.totalvalue())
print(p.mydashboard())
print(p.targetdistance())
