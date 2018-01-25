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

import time
def initialize(context):
    context.flag=False
    context.security=symbol('CASH,EUR,USD')    
    
def handle_data(context, data):
    if context.flag==False:               
        orderId=order(context.security, 100)
        order_status_monitor(orderId, target_status='Filled')
        context.flag=True

    else:
        time.sleep(10)
        display_all()
        end()
     