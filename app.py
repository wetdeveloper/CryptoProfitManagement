
stocks_targets={

                    'Alice':{ 'targets':[(12,20),(13,50),(20,60),(74,90),(2000,100)],'Savedprofits':[]},
                    'BTC':{'targets':[(20,10),(30,50)],'Savedprofits':[]}
                 }
                 #(target,take profit percentage as reach this target)
                 
totallsaved=0
for stk in stocks_targets:
                stk_quantity=int(input(f"How many {stk} do you have"))
                print(f"Stock:{stk}")
                print(f"Coin:{stk}")
                for i in range(0,len(stocks_targets[stk]['targets'])):
                    savepercentage=stocks_targets[stk]['targets'][i][1]
                    if i==0:
                        balance=stk_quantity*stocks_targets[stk]['targets'][i][0]
                        stocks_targets[stk]['Savedprofits'].append(balance*savepercentage/100)
                        balance=balance-balance*savepercentage/100
                        print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}----- Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                        totallsaved+=stocks_targets[stk]['Savedprofits'][i]
                        continue
                    balance=(balance/stocks_targets[stk]['targets'][i-1][0])*(stocks_targets[stk]['targets'][i][0])
                    stocks_targets[stk]['Savedprofits'].append(balance*savepercentage/100)
                    totallsaved+=stocks_targets[stk]['Savedprofits'][i]
                    balance=float(balance-balance*savepercentage/100)
                    print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}--------Save Percentage:{savepercentage}------ Saved profit:{stocks_targets[stk]['Savedprofits'][i]}")
                print(f"{stk} totall saved:{sum(stocks_targets[stk]['Savedprofits'])}")                        
                        
     
totallbalance=totallsaved+balance
print(f"Totall Balance:{totallbalance}")
                    
                    
                
                
                            
                    
                    
                    