# -*- coding: utf-8 -*-
"""
@author: Mariano Scandizzo

Definitions:
FA = Fixed Assets    
CA = Current Assets
OF = Owners' Funds
LTL = Long term loans
CL = Current Liabilities
TA = Total Assets
CE = Capital Employed    
"""

def gross_profit(revenue, cogs):
    """Calculate Gross profit

    Parameters
    ----------
    Revenue : int or float.
              Revenue figure for selected period.
    Cogs: int or float.
          Cost of Goods Sold figure for selected period.
    
    Returns
    -------
    Gross Profit: int or float.
                  Company's gross profit for the selected period
    """
    return revenue - cogs

def CapitalEmployed(fa, ca , cl):
    """Calculate Calpital Employed

    Parameters
    ----------
    fa: int or float.
        Fixed Assets figure for selected period.
    ca: int or float.
        Current Assets figure for selected period.
    cl: int or float.
        Current liabilities for selecteded period.

    Returns
    -------
    ce: int or float.
        Company's Capital employed for the selected period
    """
    return fa + ca - cl

def CapitalEmployedII(of, ltl):
    """Calculate Capital employed

    Parameters
    ----------
    of: int or float.
        Owner's funds figure for selected period.
    ltl: int or float.
         Long term loans figure for selected period.
    
    Returns
    -------
    ce: int or float.
        Company's capital employed for the selected period
    """
    return of + ltl

def NetWorth(fa,ca,cl,ltl):
    """Calculate Net Worth

    Parameters
    ----------
    fa: int or float.
        Fixed Assets figure for selected period.
    ca: int or float.
        Current Assets figure for selected period.
    cl: int or float.
        Current liabilities for selecteded period.
    ltl: int or float.
         Long term loans figure for selected period.
    
    Returns
    -------
    nw: int or float.
        Company's Net Worth for the selected period
    """
    return fa + ca - cl - ltl

def WorkingCapital(ca,cl):
    """Calculate Working Capital

    Parameters
    ----------
    ca: int or float.
        Current Assets figure for selected period.
    cl: int or float.
        Current liabilities for selecteded period.
    
    Returns
    -------
    wc: int or float.
        Company's Working Capital for the selected period
    """
    return ca - cl

def WorkingCapitalII(of,ltl,fa):
    """Calculate Working Capital 

    Parameters
    ----------
    of: int or float.
        Owner's funds figure for selected period.
    ltl: int or float.
         Long term loans figure for selected period.
    fa: int or float.
        Fixed assets
    
    Returns
    -------
    wc: int or float.
        Company's Working capital for the selected period
    """
    return of + ltl - fa

def ReturnTotalAssets(ebit,ta):
    """Calculate Return on Total Assets 

    Parameters
    ----------
    ebit: int or float.
        Earnings before interest & Taxes figure for selected period.
    ta: int or float.
        Total Assets figure for selected period.
    
    Returns
    -------
    rota: int or float.
        Company's Return on Total Assets for the selected period
    """
    return ebit/ta

def ReturnOnEquity(ni,nw):
    """Calculate Return on Equity 

    Parameters
    ----------
    ni: int or float.
        Net Income for selected period.
    nw: int or float.
        Net worth / Equity for selected period.
    
    Returns
    -------
    roe: int or float.
        Company's Return on Equity for the selected period
    """
    return ni / nw

def ProfitMargin(ebit,sales):
    """Calculate Profit Margin 

    Parameters
    ----------
    ebit: int or float.
        Earnings before interest & Taxes figure for selected period.
    sales: int or float.
           Sales figure for selected period.
    
    Returns
    -------
    pm: int or float.
        Company's Profit margin for the selected period
    """
    return ebit / sales

def AssetTurnover(sales,ta):
    """Calculate Asset Turnover 

    Parameters
    ----------
    ta: int or float.
        Total assets figure for selected period.
    sales: int or float.
           Sales figure for selected period.
    
    Returns
    -------
    at: int or float.
        Company's Asset turnover for the selected period
    """
    return sales/ta
    
def InventoryDays(inv,sales):
    """Calculate Inventory Days 

    Parameters
    ----------
    inv: int or float.
        Inventory figure for selected period.
    sales: int or float.
           Sales figure for selected period.
    
    Returns
    -------
    at: int or float.
        Company's Asset turnover for the selected period
    """
    InvDays = (inv/sales) * 365
    return InvDays

def CurrentRatio(ca,cl):
    """Calculate Current Ratio 

    Parameters
    ----------
    ca: int or float.
        Current Assets figure for selected period.
    cl: int or float.
        Current Liabilities figure for selected period.
    
    Returns
    -------
    cr: int or float.
        Company's Current ratio for the selected period
    """
    return ca/cl
    
def QuickRatio(ca,inv,cl):
    """Calculate Quick Ratio

    Parameters
    ----------
    ca: int or float.
        Current Assets figure for selected period.
    inv: int or float.
         Inventory figure for selected period.
    cl: int or float.
        Current Liabilites figure for the selected period.

    Returns
    -------
    qr: int or float.
        Company's Quick Ratio for the selected period
    """
    return (ca - inv) / cl

def InterestCover(ebit, interest):
    """Calculate Interest Cover

    Parameters
    ----------
    ebit: int or float.
          Earnings before interest and taxes figure for selected period.
    interest : int or float.
               Interest figure for selected period.
    
    Returns
    -------
    ic: int or float.
        Company's Interest Cover for the selected period
    """
    return ebit/interest
    
def EarningsPerShare(eat,num_shares):
    """Calculate Earnings per Share

    Parameters
    ----------
    eat: int or float.
          Earnings after taxes figure for selected period.
    num_shares : int 
                 Number of issued shares for selected period.
    
    Returns
    -------
    eps: int or float.
        Company's earnings per share for the selected period
    """
    return eat/num_shares
   
def DividensPerShare(dividends, num_shares):
    """Calculate Dividends per Share

    Parameters
    ----------
    dividends: int or float.
               Dividends figure for selected period.
    num_shares : int 
                 Number of issued shares for selected period.
    
    Returns
    -------
    dps: int or float.
        Company's dividends per share for the selected period
    """
    return dividends/ num_shares
    
def DividendsCover(eps, dps):
    """Calculate Dividends cover

    Parameters
    ----------
    eps: int or float.
         Earnings per share figure for selected period.
    dps: int or float. 
         Dividends per share for selected period.
    
    Returns
    -------
    dc: int or float.
        Company's dividends cover for the selected period
    """
    return eps / dps
    
def PayOutRatio(eps,dps):
    """Calculate Pay out Ratio

    Parameters
    ----------
    eps: int or float.
         Earnings per share figure for selected period.
    dps: int or float. 
         Dividends per share for selected period.
    
    Returns
    -------
    por: int or float.
        Company's payout ratio : dividends / earnings for the selected period
    """
    return 1/ DividendsCover(eps =eps , dps= dps)
    
def EarningYield(eps, price):
    """Calculate Earning yield

    Parameters
    ----------
    eps: int or float.
         Earnings per share figure for selected period.
    price: int or float. 
         Market price for selected period.
    
    Returns
    -------
    ey: int or float.
        Company's earning yield ratio : earnings / price for the selected period
    """
    return eps/price
    
def PriceEarnings(eps, price):
    """Calculate Price Earnings

    Parameters
    ----------
    eps: int or float.
         Earnings per share figure for selected period.
    price: int or float. 
         Market price for selected period.
    
    Returns
    -------
    pe: int or float.
        Company's price earnings ratio : price / earnings for the selected period
    """
    return 1/ EarningYield(eps = eps, price = price)
      
def RotaRatio(ProfitMargin, AssetTurnover):
    """Calculate Return on total assets

    Parameters
    ----------
    profit margin: int or float.
                   profit margin figure for selected period.
    asset turnover: int or float. 
                    asset turnover for selected period.
    
    Returns
    -------
    rotaratio: int or float.
               Company's return on total assets for the selected period
    """
    rotaratio = ProfitMargin * AssetTurnover
    return rotaratio

def WorkingCapitalToSales(ca, cl, sales):
    """Calculate Working Capital pver Sales

    Parameters
    ----------
    ca: int or float.
        Current Assets figure for selected period.
    cl: int or float.
        Current liabilities for selecteded period.
    sales: int or float.
           Sales for selecteded period.
    
    Returns
    -------
    wc: int or float.
        Company's Working Capital for the selected period
    """
    wc = WorkingCapital(ca=ca, cl=cl)
    return wc/sales
