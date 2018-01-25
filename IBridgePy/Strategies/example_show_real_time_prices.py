# -*- coding: utf-8 -*-
'''
There is a risk of loss when trading stocks, futures, forex, options and other
tradeable finacial instruments. Please trade with capital you can afford to 
lose. Past performance is not necessarily indicative of future results. 
Nothing in this computer program/code is intended to be a recommendation and/or 
solicitation to buy or sell any stocks or futures or options or any 
tradable securities/financial instruments. 
All information and computer programs provided here is for education and 
entertainment purpose only; accuracy and thoroughness cannot be guaranteed. 
Readers/users are solely responsible for how to use these information and 
are solely responsible any consequences of using these information.

If you have any questions, please send email to IBridgePy@gmail.com
'''

def initialize(context):
    pass
    
def handle_data(context, data):
    print (get_datetime().strftime("%Y-%m-%d %H:%M:%S %Z"))
    print ("EURUSD ask_price=",show_real_time_price(symbol('CASH,EUR,USD'),'ask_price'))
    print ("USDJPY ask_price=",show_real_time_price(symbol('CASH,USD,JPY'),'ask_price'))




  