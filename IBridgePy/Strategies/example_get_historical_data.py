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
    context.sec1 = symbol('SPY')
    context.secList = symbols('AAPL', 'GOOG')

def handle_data(context, data):
    # Method 1 IBridgePy function request_historical_data(security, barSize, goBack)
    # Users have more controls on this function.
    # http://www.ibridgepy.com/ibridgepy-documentation/#request_historical_data
    print ('Historical Data of %s' %(str(context.sec1,),) )
    print (request_historical_data(context.sec1, '1 day', '5 D'))
    
    # Method 2 Same as Quantopian's function
    #http://www.ibridgepy.com/ibridgepy-documentation/#datahistory_8212_similar_as_datahistory_at_Quantopian
    # data.history(security, fields, bar_count, frequency)
    context.tmp = data.history(context.secList, ['open','high', 'low', 'close'], 5, '1d')
    for i in range(len(context.secList)):
        print ('Historical Data CLOSE of %s' %(str(context.secList[i],),) )
        print (context.tmp['close'][context.secList[i]])   

    end()

          
  

