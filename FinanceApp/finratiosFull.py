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
    def __init__(self, long_term_debt = None, equity = None, current_assets = None,
                       debt = None, current_liabilities = None, assets = None,
                       depreciation = None, amortization = None, dividends_per_share = None,
                       earnings_per_share = None, stock_price = None, market_cap = None,
                       debt_issued = None, debt_repayments = None, sales = None,
                       sales_deductions = None, retained_earnings = None, liabilities = None):
        self.long_term_debt = long_term_debt
        self.equity = equity
        self.current_assets = current_assets
        self.debt = debt
        self.current_liabilities = current_liabilities
        self.assets = assets
        self.depreciation = depreciation
        self.amortization = amortization
        self.dividends_per_share = dividends_per_share
        self.earnings_per_share = earnings_per_share
        self.stock_price = stock_price
        self.market_cap = market_cap
        self.debt_issued = debt_issued
        self.debt_repayments = debt_repayments
        self.sales = sales
        self.sales_deductions = sales_deductions
        self.retained_earnings = retained_earnings
        self.liabilities = liabilities
        
        self.variables2V = {'current_assets_to_debt':('current_assets','debt',self.current_assets_to_debt),
                          'current_ratio':('current_assets','current_liabilities',self.current_ratio),
                          'debt_ratio':('debt','assets',self.debt_ratio),
                          'debt_to_equity':('debt','equity',self.debt_to_equity),
                          'dividends_payout':('dividends_per_share','earnings_per_share',self.dividends_payout),
                          'dividends_yield':('dividends_per_share','stock_price',self.dividends_yield),
                          'earnings_yield':('earnings_per_share','stock_price',self.earnings_yield),
                          'equity_to_debt':('equity','debt',self.equity_to_debt),
                          'financial_leverage_index':('assets','equity',self.financial_leverage_index),
                          'long_term_debt_to_capitalization':('long_term_debt','equity',self.long_term_debt_to_capitalization),
                          'market_to_book_ratio':('market_cap','equity',self.market_to_book_ratio),
                          'net_borrowings':('debt_issued','debt_repayments',self.net_borrowings),
                          'net_sales':('sales','sales_deductions',self.net_sales),
                          'retained_earnings_to_equity':('retained_earnings','equity',self.retained_earnings_to_equity),
                          'retained_earnings_to_assets':('retained_earnings','assets',self.retained_earnings_to_assets),
                          'stockholders_equity':('equity','assets',self.stockholders_equity),
                          'debt_to_assets':('debt','assets',self.debt_to_assets),
                          'working_capital':('current_assets','current_liabilities',self.working_capital)}
       
    def formulas(self,dataframe):
        for k,v in self.variables2V.items():
            try:
                dataframe[k]= dataframe.apply(lambda row: self.variables2V[k][2]\
                                        (row[self.variables2V[k][0]],
                                         row[self.variables2V[k][1]]),axis =1)
            except:
                print("Fields don't exist")
                pass
        
    
    def current_assets_to_debt(self,current_assets = None, debt = None):
        """
        Current assets over Total Debt
        Current assets = 
        Debt = 
        """
        try:
            if current_assets != None and debt != None:
                self.current_assets = current_assets
                self.debt = debt
                
            if self.current_assets == None or self.debt == None:
                ratioval = np.nan
            else:
                ratioval = self.current_assets / self.debt
            
            return ratioval
        except:
            pass
    
    def current_ratio(self,current_assets = None, current_liabilities = None):
        """
        Current assets over current liabilities
        """
        try:
            if current_assets != None and current_liabilities != None:
                self.current_assets = current_assets
                self.current_liabilities = current_liabilities
                
            if self.current_assets == None or self.current_liabilities == None:
                ratioval = np.nan
            else:
                ratioval = self.current_assets / self.current_liabilities
            
            return ratioval
        except:
            pass
        
    def debt_ratio(self,debt = None, assets = None):
        """
        Debt over assets
        """
        try:
            if debt != None and assets != None:
                self.debt = debt
                self.assets = assets
                
            if self.debt == None or self.assets == None:
                ratioval = np.nan
            else:
                ratioval = self.debt / self.assets
            
            return ratioval
        except:
            pass

    def dividends_payout(self,dividends_per_share = None, earnings_per_share = None):
        """
        Dividends per share over earnings per share
        """
        try:
            if dividends_per_share != None and earnings_per_share != None:
                self.dividends_per_share = dividends_per_share
                self.earnings_per_share = earnings_per_share
                
            if self.dividends_per_share == None or self.earnings_per_share == None:
                ratioval = np.nan
            else:
                ratioval = self.dividends_per_share / self.earnings_per_share
            
            return ratioval
        except:
            pass 
    
    def dividends_yield(self,dividends_per_share = None, stock_price = None):
        """
        Dividends per share over current stock price
        """
        try:
            if dividends_per_share != None and stock_price != None:
                self.dividends_per_share = dividends_per_share
                self.stock_price = stock_price
                
            if self.dividends_per_share == None or self.stock_price == None:
                ratioval = np.nan
            else:
                ratioval = self.dividends_per_share / self.stock_price
            
            return ratioval
        except:
            pass
        
    def earnings_yield(self,earnings_per_share = None, stock_price = None):
        """
        earnings per share over stock price
        """
        try:
            if earnings_per_share != None and stock_price != None:
                self.earnings_per_share = earnings_per_share
                self.stock_price = stock_price
                
            if self.earnings_per_share == None or self.stock_price == None:
                ratioval = np.nan
            else:
                ratioval = self.earnings_per_share / self.stock_price
            
            return ratioval
        except:
            pass
        
        
    def equity_to_debt(self,equity = None, debt = None):
        """
        Current assets over current liabilities
        """
        try:
            if equity != None and debt != None:
                self.equity = equity
                self.debt = debt
                
            if self.equity == None or self.debt == None:
                ratioval = np.nan
            else:
                ratioval = self.equity / self.debt
            
            return ratioval
        except:
            pass
        
        
    def financial_leverage_index(self,assets = None, equity = None):
        """
        assets over equity
        """
        try:
            if assets != None and equity != None:
                self.assets = assets
                self.equity = equity
                
            if self.assets == None or self.equity == None:
                ratioval = np.nan
            else:
                ratioval = self.assets / self.equity
            
            return ratioval
        except:
            pass
        
        
    def long_term_debt_to_capitalization(self,long_term_debt = None, equity = None):
        """
        long term debt over long term debt plus equity
        """
        try:
            if long_term_debt != None and equity != None:
                self.long_term_debt = long_term_debt
                self.equity = equity
                
            if self.long_term_debt == None or self.equity == None:
                ratioval = np.nan
            else:
                ratioval = self.long_term_debt / (self.long_term_debt + self.equity)
            
            return ratioval
        except:
            pass
        
    def market_to_book_ratio(self,market_cap = None, equity = None):
        """
        Market capitalization over book value of equity
        """
        try:
            if market_cap != None and equity != None:
                self.market_cap = market_cap
                self.equity = equity
                
            if self.market_cap == None or self.equity == None:
                ratioval = np.nan
            else:
                ratioval = self.market_cap / self.equity
            
            return ratioval
        except:
            pass
        
    def net_borrowings(self,debt_issued = None, debt_repayment = None):
        """
        Debt issued during fiscal year less debt repayments
        """
        try:
            if debt_issued != None and debt_repayment != None:
                self.debt_issued = debt_issued
                self.debt_repayments = debt_repayment
                
            if self.debt_issued == None or self.debt_repayments == None:
                ratioval = np.nan
            else:
                ratioval = self.debt_issued - self.debt_repayments
            
            return ratioval
        except:
            pass
        
        
    def net_sales(self,sales = None, sales_deductions = None):
        """
        Current assets over current liabilities
        """
        try:
            if sales != None and sales_deductions != None:
                self.sales = sales
                self.sales_deductions = sales_deductions
                
            if self.sales == None or self.sales_deductions == None:
                ratioval = np.nan
            else:
                ratioval = self.sales - self.sales_deductions
            
            return ratioval
        except:
            pass
        
        
    def retained_earnings_to_equity(self,retained_earnings = None, equity = None):
        """
        Current assets over current liabilities
        """
        try:
            if retained_earnings != None and equity != None:
                self.retained_earnings = retained_earnings
                self.equity = equity
                
            if self.retained_earnings == None or self.equity == None:
                ratioval = np.nan
            else:
                ratioval = self.retained_earnings / self.equity
            
            return ratioval
        except:
            pass
        
        
    def retained_earnings_to_assets(self,retained_earnings = None, assets = None):
        """
        Current assets over current liabilities
        """
        try:
            if retained_earnings != None and assets != None:
                self.retained_earnings = retained_earnings
                self.assets = assets
                
            if self.retained_earnings == None or self.assets == None:
                ratioval = np.nan
            else:
                ratioval = self.retained_earnings / self.assets
            
            return ratioval
        except:
            pass
        
        
    def stockholders_equity(self,equity = None, assets = None):
        """
        Current assets over current liabilities
        """
        try:
            if equity != None and assets != None:
                self.equity = equity
                self.assets = assets
                
            if self.equity == None or self.assets == None:
                ratioval = np.nan
            else:
                ratioval = self.equity / self.assets
            
            return ratioval
        except:
            pass
        
        
    def debt_to_assets(self,debt = None, assets = None):
        """
        Current assets over current liabilities
        """
        try:
            if debt != None and assets != None:
                self.debt = debt
                self.assets = assets
                
            if self.debt == None or self.assets == None:
                ratioval = np.nan
            else:
                ratioval = self.debt / self.assets
            
            return ratioval
        except:
            pass
        
        
    def working_capital(self,current_assets = None, current_liabilities = None):
        """
        Current assets over current liabilities
        """
        try:
            if current_assets != None and current_liabilities != None:
                self.current_assets = current_assets
                self.current_liabilities = current_liabilities
                
            if self.current_assets == None or self.current_liabilities == None:
                ratioval = np.nan
            else:
                ratioval = self.current_assets - self.current_liabilities
            
            return ratioval
        except:
            pass