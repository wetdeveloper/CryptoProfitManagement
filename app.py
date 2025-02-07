def reinvest(savedprofit,previousPrice,sellprice,stk,currentprice,autoreinvest=True):#currentPrice=previous price
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
                return savedprofit
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
            return savedprofit
        else:
            print("lack of ballance.try at next target again.you didn't use your saved profit\n")
            return savedprofit

        

# sundae 37198 MIN 11082 DOG 45938   Bar 25  Alice 85


stocks_targets={

                
                    'SUNDAE':{'targets':[(0.24,70),(0.48,80),(3,100)],'Savedprofits':[]},
                    'MIN':{'targets':[(0.5,50),(1,80),(3,100)],'Savedprofits':[]},
                    'DOG':{'targets':[(0.1,50),(0.2,80),(0.4,90),(0.7,100)],'Savedprofits':[]},
                    'BAR':{'targets':[(30.20,70),(70,100)],'Savedprofits':[]},
                    'Alice':{'targets':[(20,70),(40,70),(58,100)],'Savedprofits':[]},
                    
                 }
                 
reinvestments=[]#['token','entry price',sell price,reinvested money$']
investmentpercentage=False #for exampe 10% savedprofit supposed to be invested
reinvestmentactive=False
totallbalance=0                 
totallsaved=0
autoreinvest=False #if false=>reinvest manualy
for stk in stocks_targets:
                stk_quantity=int(input(f"How many {stk} do you have: "))
                print(f"Stock:{stk}")
                for i in range(0,len(stocks_targets[stk]['targets'])):
                    savepercentage=stocks_targets[stk]['targets'][i][1]
                    if i==0:
                        balance=stk_quantity*stocks_targets[stk]['targets'][i][0]
                        savedprofit=balance*savepercentage/100
                        totallsaved+=savedprofit
                        stocks_targets[stk]['Savedprofits'].append(savedprofit)
                        balance=balance-savedprofit
                        print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}----- Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                        print(f"{stk} totall saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                        print(f"Totall saved profit:{totallsaved}")
                        print("----------------------------------------------------------------------------------------------------------------")
                        continue
                    previousPrice=stocks_targets[stk]['targets'][i-1][0]
                    balance=(balance/previousPrice)*(stocks_targets[stk]['targets'][i][0])
                    savedprofit=balance*savepercentage/100
                    balance=float(balance-savedprofit)
                    currentprice=stocks_targets[stk]['targets'][i][0]
                    if reinvestmentactive:
                        savedprofit=reinvest(savedprofit,previousPrice,stocks_targets[stk]['targets'][i][0],stk,currentprice,autoreinvest)
                        #balance+=savedprofit
                        print(f"savedprofit after reinvesting:{savedprofit}")
                    stocks_targets[stk]['Savedprofits'].append(savedprofit)
                    totallsaved+=savedprofit
                    print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}------ Saved profit:{savedprofit}")
                    print(f"{stk} totall saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                    print(f"Totall saved profit:{totallsaved}")
                    print("----------------------------------------------------------------------------------------------------------------------------")
                totallbalance+=balance
                
print(f"reinvestments:{reinvestments}")
reinvestmentsmade=sum([item[4] for item in reinvestments])
print(f"Totall Balance:{totallbalance}")
print(f"reinvestment made money:{reinvestmentsmade}$")
totallbalance+=sum([item[4] for item in reinvestments])
print(f"totalsaved:{totallsaved}")
print(f"Totall Balance(Balance+reinvestment made money+totall saved profit:{totallbalance+totallsaved}$")
                    
                    
                
                
                            
