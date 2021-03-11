import numpy as np
import numpy_financial as npf 


def bond_pricing(min, max, coupon, num=20):
    """
    Net present value simulation 
    min = minimum discount rate 
    max = maximum discount rate
    coupon = sequence of values representing a cash flow stream
    num = number of simulation steps, default value = 20
    """
    rates = np.linspace(start=min/100, stop=max/100, num=num)
    coupon.insert(0, 0)
    prices = []
    for rate in rates:
        price = npf.npv(rate, coupon)
        prices.append(price)

    return prices

def bond_pricing_pythonic(min,max,coupon,num=20):
    """
    Net present value simulation 
    min = minimum discount rate 
    max = maximum discount rate
    coupon = sequence of values representing a cash flow stream
    num = number of simulation steps, default value = 20
    IMPORTANT = the 1st element in the coupon array should be 0, 
    followed by the actual array values
    """
    return [npf.npv(rate, coupon) for rate in np.linspace(start=min, stop=max, num=num)]

def equity_cost(rf,beta,mkt_premium):
    """
    Cost of equity calculation following CAPM

    rf = risk free

    beta = stock volatility measure with respect to the market

    mkt_premium = additional return an investor expects for holding a risky market
    portfolio instead of risk free assets

    Equity Required return = risk free + beta * Market Risk Premium
    """
    return rf + beta * mkt_premium

def h_model(div,re,gh,gs,h):
    """
    H-model valuation 

    div =  Current dividen per share/ Current Total Dividend
    
    re = required return on equity 

    gh = growth rate during high growth period

    gs = growth rate during stable growth period

    h = Half-life of the high growth period

                         dividends x (1 + stable growth rate)                dividends x H factor (high growth rate + stable growth rate)
    Company Value =    -----------------------------------------------  +   --------------------------------------------------------------
                     (required return on equity - stable growth rate)            (required return on equity - stable growth rate)

    """
    term1 = (div * (1 + gs))/ (re - gs)
    term2 = (div * h * (gh - gs)) / (re - gs)

    return term1 + term2

def gordon_2_stage_stable(div,rehg,resg,gh,gs,n):
    """
    Calculates 2 stage dividend discount model
    
    div =  Current dividen per share/ Current Total Dividend
    
    rehg = required return on equity during high growth phase

    resg = required return on equity during stable growth phase

    gh = growth rate during high growth period

    gs = growth rate during stable growth period

    n = number of high growth periods

                                                              [ (1+ high growth rate) ^ high growth periods             ]
                   dividends_0 x (1+ high growth rate) x  1 - | ------------------------------------------------------- |
                                                              [ (1+ high growth required return) ^ high growth periods  ]
    Company Value= ------------------------------------------------------------------------------------------------------ +
                                       (high growth required return - high growth rate)                                          

                                                        dividends_high_growth_period_+_1
                 +  ------------------------------------------------------------------------------------------------------------ 
                     (stable growth required return - high growth rate) x (1+ high growth required return) ^ high growth periods

    """
    
    term1 = (div * (1+ gh) * (1 - ((1+gh) ** n)/(1+rehg) ** n))/(rehg - gh)
    term2 = (div * (1+gh) ** n)/ ((resg - gs) * (( 1 + gh) ** n))
    return term1 + term2

def div_growth_calculator(g,n,pay,div=0,ear=0):
    """
    It calculates the dividen or earnings growth for a given
    number of periods and specified growth rate and payout ratio

    div = Current dividen per share/ Current Total Dividend

    ear = Current earnings per share/ Current Total earnings
    
    g = growth rate

    n = number of periods

    pay = payout ratio
    """
    x = 0
    sequence = []
    
    while x < n:
        if ear == 0 and div != 0:
            div *= (1+g) 
            sequence.append(div)
            x += 1
        elif ear != 0 and div == 0:
            ear *= (1+g)
            sequence.append(ear*pay)
            x += 1

    return sequence

def px_comp(g,n,pay,re,div=0,ear=0):
    """
    Calculates company price 

    """
    flows = div_growth_calculator(g=g,n=n,pay=pay,div=div,ear=ear)
    flows.insert(0,0)
    result = npf.npv(re,flows)
    
    return result

def terminal_div(re,g,ear,pays):
    """
    Calculates terminal value based on:

    re= required return on equity 
    g = stable growth rate
    ear = stable year earnings
    pays = payout ratio long term growth period

    It follows standard perpetuity calculation

                          Earnings x (1 + stable growth rate) * payout ratio 
    Terminal Value =    -----------------------------------------------------   
                          (required return on equity - stable growth rate)

    Function can be used for Classic Constant Gordon Growth model calculation 
    """
    
    return (ear *(1+g) * pays) /(re - g)

def gaps_calculation(low,high,n):
    """
    Calculates the linear increment between start and end 
    given a predetermined number of steps

    low = range lowest value
    high = range highest value
    n = number of steps
    """
    return (high-low)/n

def div_transition(ear,gh,gs,payh,pays,reh,res,n):
    """
    Calculates the transition period values for earnings and dividends in a
    3 stage dividend discount model

    ear = earning per share / total earnings
    gh = growth during high growth stage
    gs = stable long term growth
    payh = payout ratio high growth phase
    pays = payout ratio long term growth period 
    reh = equity required return high growth phase
    res = equity required return stable growth phase
    n = transition period number of periods

    Assumptions: 
    1. It assumes that payout ratio growths over time
    2. It assumes that equity required return decreases as company matures

                               earnings_period_n x growth rate_period_n x payout_ration_period_n
    transition value = Sum(   ------------------------------------------------------------------- )
                                          (1 + required_equity_return_period_n)
    """
    growth_step = gaps_calculation(high=gh,low=gs,n=n)
    payout_step = gaps_calculation(high=pays,low=payh,n=n)
    re_step = gaps_calculation(high=reh,low=res,n=n)

    x = 0
    earnings = []
    dividends = []
    growths = []
    payouts = []
    equity_cost = []
    discounted_div = []

    while x < n:
        # update of period parameters
        gh -= growth_step
        payh += payout_step
        reh -= re_step

        # run calculations
        ear *= (1+gh)
        div = ear * payh
        re_disc = 1 + (reh) 

        # store data
        earnings.append(ear)
        dividends.append(div)
        growths.append(gh)
        payouts.append(payh)
        equity_cost.append(re_disc)

        #calculate npv 
        discounted_div.append(div/np.prod(equity_cost))
        x += 1

    return earnings,dividends,growths,payouts,equity_cost,discounted_div

def div_high_growth(ear,gh,payh,reh,n):
    """
    Calculates the high growth period values for earnings and dividends in a
    3 stage dividend discount model

    ear = earning per share / total earnings
    gh = growth during high growth stage
    payh = payout ratio high growth phase
    reh = equity required return high growth phase
    n = transition period number of periods

    Assumptions: 
    1. It assumes that payout ratio growths over time
    2. It assumes that equity required return decreases as company matures

                             Earnings_period_n x (1 + high growth rate) x high growth period payout ratio
    High growth value =Sum( ------------------------------------------------------------------------------- )
                                 ( 1 + high growth period required equity return ) ^ n
    """                
    x = 0
    earnings_high = []
    dividends_high = []
    growths_high = []
    payouts_high = []
    equity_cost_high = []
    discounted_div_high = []

    while x < n:
        # run calculations
        ear *= (1+gh)
        div = ear * payh
       
        # store data
        earnings_high.append(ear)
        dividends_high.append(div)
        growths_high.append(gh)
        payouts_high.append(payh)
        equity_cost_high.append(1 + reh)

        #calculate npv
        discounted_div_high.append(div/np.prod(equity_cost_high))
        x += 1

    return earnings_high,dividends_high,growths_high,payouts_high,equity_cost_high,discounted_div_high

def ddm_3_stage(ear,gh,gs,payh,pays,reh,res,nh,nt):
    """
    Calculates the transition period values for earnings and dividends in a
    3 stage dividend discount model

    It combines 3 preceding functions to calculate:
    a. high growth period
    b. transition period
    c. terminal value

    ear = earning per share / total earnings
    gh = growth during high growth stage
    gs = stable long term growth
    payh = payout ratio high growth phase
    pays = payout ratio long term growth period 
    reh = equity required return high growth phase
    res = equity required return stable growth phase
    nh = high growth number of periods
    nt = transition period number of periods

    Assumptions: 
    1. It assumes that payout ratio growths over time
    2. It assumes that equity required return decreases as company matures
    """
    # run high growth period
    ear_high, div_high, gro_high, pay_high, eq_cst_high, disc_div_high = \
        div_high_growth(ear=ear, gh=gh, payh=payh,reh=reh,n=nh)

    # run transition growth period
    ear_tran, div_tran, gro_tran, pay_tran, eq_cst_tran, disc_div_tran = \
        div_transition(ear=ear_high[-1],gh=gh,gs=gs,payh=payh,pays=pays,reh=reh,res=res,n=nt)

    disc_div_tran_today = [ (x / np.prod(eq_cst_high)) for x in disc_div_tran]

    # run terminal value period
    terminal_value = terminal_div(re=res,g=gs,ear=ear_tran[-1],pays=pays)

    terminal_value_today = terminal_value / (np.prod(eq_cst_high) * np.prod(eq_cst_tran))

    # putting together the 3 stages
    earnings = ear_high + ear_tran
    dividens = div_high + div_tran
    growth_rate = gro_high + gro_tran
    payout_ratio = pay_high + pay_tran
    equity_cost = eq_cst_high + eq_cst_tran
    discounted_dividends = disc_div_high + disc_div_tran
    
    # Company value Calculation
    company_value = sum(discounted_dividends)+ terminal_value_today

    return company_value, terminal_value, earnings, dividens, growth_rate, \
        payout_ratio, equity_cost, discounted_dividends, terminal_value_today



