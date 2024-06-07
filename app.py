
stocks_targets={

                    'Alice':{ 'targets':[(12,20),(13,50),(20,60),(74,100),(2000,100)]},
                    'BTC':{'targets':[(20,10),(30,50)]}
                 }
                 
                 
for stk in stocks_targets:
                stk_quantity=int(input(f"How many {stk} do you have"))
                print(f"Stock:{stk}")
                balance=0
                print(f"Coin:{stk}")
                for i in range(0,len(stocks_targets[stk]['targets'])):
                    savepercentage=stocks_targets[stk]['targets'][i][1]
                    if i==0:
                        balance=stk_quantity*stocks_targets[stk]['targets'][i][0]
                        balance=balance-balance*savepercentage/100
                        print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}")
                        continue
                    
                    balance=(balance/stocks_targets[stk]['targets'][i-1][0])*(stocks_targets[stk]['targets'][i][0])
                    balance=float(balance-balance*savepercentage/100)
                    print(f"TP{i+1}:{stocks_targets[stk]['targets'][i][0]} ---- Balance:{balance}")
                    
                        
                        
      
                
                    
                    
                
                
                            
                    
                    
                    