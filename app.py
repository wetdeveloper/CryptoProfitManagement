def reinvest(savedprofit):
    if input(f"You have {savedprofit}$ saved profit.Do you want reinvest your taken profit again?Y/N")=="Y":
        count=0
        for i in range(len(list(stocks_targets))):
            print(f"{i} {list(stocks_targets)[i]})")
        reinvestchoice=int(input("what you wanna reinvest?enter the number"))
        buyprice=float(input("What price you wanna buy?"))
        investmentAmount=int(input(f"You have {savedprofit} saved profit. how much you wanna invest?enter the amount."))
        if investmentAmount>0 and investmentAmount<savedprofit:
            reinvestments.append([list(stocks_targets)[reinvestchoice],buyprice,investmentAmount])
            savedprofit=savedprofit-investmentAmount
            print("Well done")
            return savedprofit
        else:
            print("lack of ballance")
            return 0
    return 0
            
        
        
            


stocks_targets={

                    'Alice':{ 'targets':[(4.968,20),(8.37,30),(14.89,50),(20.22,70),(32.696,80),(45,80),(65,100)],'Savedprofits':[],},
                    'ADA':{'targets':[(2.30,10),(3.5,30),(4.60,50),(6,60),(9,90)],'Savedprofits':[]}
                 }
                 #(target,take profit percentage as reach this target)
reinvestments=[]#['token','entry price',how much saved profit money']
                 
totallbalance=0                 
totallsaved=0
for stk in stocks_targets:
                stk_quantity=int(input(f"How many {stk} do you have"))
                print(f"Stock:{stk}")
                for i in range(0,len(stocks_targets[stk]['targets'])):
                    savepercentage=stocks_targets[stk]['targets'][i][1]
                    if i==0:
                        balance=stk_quantity*stocks_targets[stk]['targets'][i][0]
                        savedprofit=balance*savepercentage/100
                        #savedprofit-=reinvest(savedprofit)
                        totallsaved+=savedprofit
                        
                        stocks_targets[stk]['Savedprofits'].append(savedprofit)
                        balance=balance-savedprofit
                        print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}----- Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                        totallsaved+=stocks_targets[stk]['Savedprofits'][i]
                        continue
                    balance=(balance/stocks_targets[stk]['targets'][i-1][0])*(stocks_targets[stk]['targets'][i][0])
                    savedprofit=balance*savepercentage/100
                    #savedprofit-=reinvest(savedprofit)
                    stocks_targets[stk]['Savedprofits'].append(savedprofit)
                    #totallsaved+=stocks_targets[stk]['Savedprofits'][i]
                    totallsaved+=savedprofit
                    balance=float(balance-savedprofit)
                    print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}------ Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                print(f"{stk} totall saved:{sum(stocks_targets[stk]['Savedprofits'])}")
                totallbalance+=balance
                        
     
#totallbalance=totallsaved-totalbalance
print(f"reinvestments:{reinvestments}")
print(f"totalsaved:{totallsaved}")
print(f"Totall Balance:{totallbalance}$")
print(f"Totall Balance:{totallbalance*60000}rial")
                    
                    
                
                
                            
                    
                    
                    
