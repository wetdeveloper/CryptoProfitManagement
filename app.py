from pycoingecko import CoinGeckoAPI

class Portfolio(object):
    
    def __init__(self,myassets):
        self.myassets=myassets
        cg = CoinGeckoAPI()
        assetslist=",".join([asset for asset in self.myassets])
        self.assetsdata=cg.get_price(ids=assetslist, vs_currencies='usd')
        
    
    def mydashboard(self):
        mydashboard=[]
        for asset in self.assetsdata:
            coin=asset
            price=self.assetsdata[asset]['usd']
            quantity=self.myassets[asset]['Q']
            mydashboard.append((asset,price*quantity))
        return mydashboard
        
    def totalvalue(self):
        tvalue=sum(item[1] for item in self.mydashboard())
        return tvalue
        
        
    def targetdistance(self):
        """
            calculate curent price distance from next taking profit targets by percentage
        """
        for asset in self.assetsdata:
            for profitTargt in self.myassets[asset]['targets']:
                print(f"asset:{asset} , target:{profitTargt[0]} , current price:{self.assetsdata[asset]['usd']} ")
                if self.assetsdata[asset]['usd']>=profitTargt[0]:#proftTargt[1]=taking profit percentage in stocks_targets,myassets=stocks_targets
                    pass
                else:
                    pass
            
                
        
        


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

                
                    'sundaeswap':{'targets':[(0.03,70),(0.06,40),(0.1,60),(0.15,70),(0.24,80),(0.48,90),(3,100)],'Savedprofits':[],'Q':31198},
                    'minswap':{'targets':[(0.1,70),(0.3,50),(0.5,70),(1,80),(3,100)],'Savedprofits':[],'Q':13120},
                    'dog-go-to-the-moon-rune':{'targets':[(0.01,70),(0.02,30),(0.3,50),(0.1,70),(0.2,80),(0.4,90),(0.7,100)],'Savedprofits':[],'Q':42064},
                    'indigo-dao-governance-tok':{'targets':[(6.5,70),(30,70),(50,100)],'Savedprofits':[],'Q':38},
                    'ski-mask-dog':{'targets':[(0.3,70),(0.52,50),(0.82,70),(1.13,80),(1.43,100)],'Savedprofits':[],'Q':702},
                    
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
                    stk_quantity=stocks_targets[stk]['Q']
                    print(f"Stock:{stk}")
                    for i in range(0,len(stocks_targets[stk]['targets'])):
                        savepercentage=stocks_targets[stk]['targets'][i][1]
                        if i==0:
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

