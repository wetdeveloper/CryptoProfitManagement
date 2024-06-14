def reinvest(savedprofit,previousPrice,sellprice,stk,autoreinvest=True):#currentPrice=previous price
        for i in range(len(list(stocks_targets))):
            print(f"{i} {list(stocks_targets)[i]}")
        if not(autoreinvest) and input(f"You have {savedprofit}$ saved profit.Do you want reinvest your taken profit again?Y/N:  ")=="Y":
            print(f"Your previous price level at {stk} is {previousPrice}")
            reinvestchoice=int(input("what coin do you want to reinvest in?enter the number: "))
            print(f"Your investing on {list(stocks_targets)[reinvestchoice]}")
            buyprice=float(input("What price you wanna buy at?"))
            investmentAmount=float(input(" how much money you wanna invest?enter the amount$: "))
        else:
            #auto reinvest
            reinvestchoice=stk
            buyprice=previousPrice
            investmentAmount=savedprofit
        if investmentAmount>0 and investmentAmount<=savedprofit:
            if not(autoreinvest):
                reinvestments.append([list(stocks_targets)[reinvestchoice],buyprice,sellprice,investmentAmount])
            else:
                reinvestments.append([reinvestchoice,buyprice,sellprice,investmentAmount,investmentAmount/buyprice*sellprice])#profit is how much we get by buying at previous price and selling at current price
            savedprofit=savedprofit-investmentAmount
            print("Well done \n")
            return savedprofit
        else:
            print("lack of ballance \n")
            return 0


stocks_targets={

                    'Alice':{ 'targets':[(4.968,20),(8.37,30),(14.89,50),(20.22,70),(32.696,80),(45,80),(65,100)],'Savedprofits':[],},
                    'ADA':{'targets':[(2.30,10),(3.5,30),(4.60,50),(6,60),(9,90)],'Savedprofits':[]}
                 }
                 #(target,take profit percentage as reach this target)
                 
reinvestments=[]#['token','entry price',sell price,reinvested money$']

                 
totallbalance=0                 
totallsaved=0
autoreinvest=True
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
                    savedprofit=reinvest(savedprofit,previousPrice,stocks_targets[stk]['targets'][i][0],stk)
                    balance+=savedprofit
                    print(f"savedprofit after reinvesting:{savedprofit}")
                    stocks_targets[stk]['Savedprofits'].append(savedprofit)
                    totallsaved+=savedprofit
                    print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}------ Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                    print(f"{stk} totall saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                    print(f"Totall saved profit:{totallsaved}")
                    print("----------------------------------------------------------------------------------------------------------------------------")
                totallbalance+=balance
                
print(f"reinvestments:{reinvestments}")
totallbalance+=sum([item[4] for item in reinvestments])
print(f"totalsaved:{totallsaved}")
print(f"Totall Balance:{totallbalance}$")
                    
                    
                
                
                            
                    
                    
                    
