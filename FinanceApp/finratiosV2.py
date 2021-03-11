import pandas as pd
import numpy as np

class FinRatios(object):
    """
    This class contains all the financial ratios which contain 2 input variables.
    A dictionary (variables2V) has been created where each financial ratio (key)
    has a tuple value with the input variables name as well as the formula to calculate
    
    ratios can be used calculate time series in a pandas dataframe as well as cross sectional
    data by calling the function or assigning the desired values to each input attibute and later on 
    run the formula.
    """
    def __init__(self, equity = None, current_assets = None,
                       debt = None, current_liabilities = None):
        self.equity = equity
        self.current_assets = current_assets
        self.debt = debt
        self.current_liabilities = current_liabilities
                
        self.variables2V = {'debt_to_equity':('Equity','Debt',self.debt_to_equity),
                            'working_capital':('CurrentAssets','CurrentLiabilities',self.working_capital)}
       
    def formulas(self,dataframe):
        for k,v in self.variables2V.items():
            dataframe[k]= dataframe.apply(lambda row: self.variables2V[k][2]\
                                        (row[self.variables2V[k][0]],
                                         row[self.variables2V[k][1]]),axis =1)
            
        
    def debt_to_equity(self,equity = None, debt = None):
        """
        Current assets over current liabilities
        """
        
        if equity == None and debt == None:
            equity = self.equity
            debt = self.debt
                    
        else:
            ratioval = equity / debt
        
        return ratioval
           
        
        
        
    def working_capital(self,current_assets = None, current_liabilities = None):
        """
        Current assets over current liabilities
        """
        
        if current_assets == None and current_liabilities == None:
            current_assets = self.current_assets
            current_liabilities = self.current_liabilities
            ratioval = current_assets - current_liabilities
            
        else:
            ratioval = current_assets - current_liabilities
        
        return ratioval
        