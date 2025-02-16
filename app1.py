def reinvest(savedprofit,previousPrice,sellprice,stk,currentprice,reinvestments,autoreinvest=True):#currentPrice=previous price
        for i in range(len(list(stocks_targets))):
            print(f"{i} {list(stocks_targets)[i]}")
        print(f"currentPrice is {currentprice}")
        if not (autoreinvest):
            if input(f"You have {savedprofit}$ saved profit.Do you want reinvest your taken profit again?Y/N:  ")=="Y":
                print(f"Your previous price level at {stk} is {previousPrice}")
                reinvestchoice=int(input("what coin do you want to reinvest in?enter the number: "))
                print(f"Your investing on {list(stocks_targets)[reinvestchoice]}")
                buyprice=float(input("What price you wanna buy at?"))
                investmentAmount=float(input(" how much money you wanna invest?enter the amount$: "))
            else:
                print("You did not reinvest.")
                return savedprofit,reinvestments
        elif autoreinvest:   
            reinvestchoice=stk
            buyprice=previousPrice
            investmentAmount=savedprofit
        if investmentAmount>0 and investmentAmount<=savedprofit:
            if not(autoreinvest):
                reinvestments.append([list(stocks_targets)[reinvestchoice],buyprice,sellprice,investmentAmount,investmentAmount/buyprice*sellprice])
            else:
                reinvestments.append([reinvestchoice,buyprice,sellprice,investmentAmount,investmentAmount/buyprice*sellprice])#profit is how much we get by buying at previous price and selling at current price
            savedprofit=savedprofit-investmentAmount
            print("Well done \n")
            return savedprofit,reinvestments
        else:
            print("lack of ballance.try at next target again.you didn't use your saved profit\n")
            return savedprofit,reinvestments

        




stocks_targets={
"""
Best Senario
"""
                
                    'SUNDAE':{'targets':[(0.24,70),(0.48,80),(3,100)],'Savedprofits':[]},
                    'MIN':{'targets':[(0.5,70),(1,80),(3,100)],'Savedprofits':[]},
                    'DOG':{'targets':[(0.1,70),(0.2,80),(0.4,90),(0.7,100)],'Savedprofits':[]},
                    'BAR':{'targets':[(30.20,70),(70,100)],'Savedprofits':[]},
                    'Alice':{'targets':[(20,70),(40,70),(58,100)],'Savedprofits':[]},
                    
                 }
                 



stocks_targets1={
"""
Worst Senario
Result=>tbalance=6859.858$
        tbalance if renvestment active=11060.573072463769$$

"""
                
                    'SUNDAE':{'targets':[(0.042,50),(0.1,100)],'Savedprofits':[]},
                    'MIN':{'targets':[(0.16,50),(0.28,100)],'Savedprofits':[]},
                    'DOG':{'targets':[(0.02,100),(0.03,100)],'Savedprofits':[]},
                    'BAR':{'targets':[(9.20,70),(13,100)],'Savedprofits':[]},
                    'Alice':{'targets':[(5,70),(12,100)],'Savedprofits':[]},
                    
                 }
                 

def profitcalculator(stocks_targets):
    reinvestments=[]#['token','entry price',sell price,reinvested money$']
    # investmentpercentage=True #for exampe 10% savedprofit supposed to be invested
    reinvestmentactive=False
    totalbalance=0                 
    totalsaved=0
    autoreinvest=False #if false=>reinvest manualy
    balance=0
    print(stocks_targets)
    for stk in stocks_targets:
                    stk_quantity=int(input(f"How many {stk} do you have: "))
                    print(f"Stock:{stk}")
                    for i in range(0,len(stocks_targets[stk]['targets'])):
                        print(f"i={i}")
                        savepercentage=stocks_targets[stk]['targets'][i][1]
                        if i==0:
                            print("zone Zero")
                            balance=stk_quantity*stocks_targets[stk]['targets'][i][0]
                            savedprofit=balance*savepercentage/100
                            totalsaved+=savedprofit
                            stocks_targets[stk]['Savedprofits'].append(savedprofit)
                            balance=balance-savedprofit
                            print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}$--------Save Percentage:{savepercentage}----- Saved profit:{stocks_targets[stk]['Savedprofits'][i]}$")
                            print(f"{stk} total saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                            print(f"total saved profit:{totalsaved}")
                            print("--------------------------------------------------------------------------------------------")
                        else:
                            print("zone One")
                            previousPrice=stocks_targets[stk]['targets'][i-1][0]
                            balance=(balance/previousPrice)*(stocks_targets[stk]['targets'][i][0])
                            savedprofit=balance*savepercentage/100
                            balance=float(balance-savedprofit)
                            currentprice=stocks_targets[stk]['targets'][i][0]
                            if reinvestmentactive:
                                savedprofit,reinvestments=reinvest(savedprofit,previousPrice,stocks_targets[stk]['targets'][i][0],stk,currentprice,reinvestments,autoreinvest)
                                #balance+=savedprofit
                                print(f"savedprofit after reinvesting:{savedprofit}")
                            stocks_targets[stk]['Savedprofits'].append(savedprofit)
                            totalsaved+=savedprofit
                            print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}------ Saved profit:{savedprofit}")
                            print(f"{stk} total saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                            print(f"total saved profit:{totalsaved}")
                        print("----------------------------------------------------------------------------------------------------------------------------")
                    totalbalance+=balance
    return [reinvestments,totalbalance,totalsaved]
    



def main():
    # sundae 37198 MIN 11082 DOG 45938   Bar 25  Alice 85
    reinvestments,totalbalance,totalsaved=profitcalculator(stocks_targets1)
    print(f"reinvestments:{reinvestments}")
    reinvestmentsmade=sum([item[4] for item in reinvestments])
    print(f"total Balance:{totalbalance}")
    print(f"reinvestment made money:{reinvestmentsmade}$")
    totalbalance+=sum([item[4] for item in reinvestments])
    print(f"totalsaved:{totalsaved}")
    print(f"total Balance(Balance+reinvestment made money+total saved profit:{totalbalance+totalsaved}$")
    
main()
                    
                    
                
                
                            
