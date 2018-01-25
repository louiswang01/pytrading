import time
import datetime as dt
import pytz
import pandas as pd
from sys import exit

def localTzname():
    is_dst=time.localtime().tm_isdst 
    if time.daylight and is_dst>0:
        offsetHour = time.altzone / 3600
    else:
        offsetHour = time.timezone / 3600
    return 'Etc/GMT%+d' % offsetHour
    
def dt_to_utc_in_seconds(a_dt, showTimeZone=None):
    '''
    dt.datetime.fromtimestamp
    the return value depends on local machine timezone!!!!
    So, dt.datetime.fromtimestamp(0) will create different time at different machine
    '''
    #print (__name__+'::dt_to_utc_in_seconds: EXIT, read function comments')
    #exit()
    if a_dt.tzinfo==None:
        if showTimeZone:
            a_dt=showTimeZone.localize(a_dt)
        else:
            a_dt=pytz.utc.localize(a_dt)
            #print(__name__+'::dt_to_utc_in_seconds:EXIT, a_dt is native time, showTimeZone must be not None')
            #exit()
    return (a_dt.astimezone(pytz.utc)-dt.datetime(1970,1,1,0,0, tzinfo=pytz.utc)).total_seconds()

def if_market_is_open(dt_aTime, start='9:30', end='16:00', early_end='13:00', version='true_or_false'):

    holiday=[dt.date(2015,11,26),dt.date(2015,12,25),\
             dt.date(2016,1,1),dt.date(2016,1,18),dt.date(2016,2,15),
             dt.date(2016,3,25),dt.date(2016,5,30),dt.date(2016,7,4),
             dt.date(2016,9,5),dt.date(2016,11,24),dt.date(2016,12,26)]
    earlyClosing=[dt.date(2015,11,27), dt.date(2015,12,24)] 
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    if dt_aTime.tzinfo==None:
        print ('small_tools::if_market_is_open: cannot handle timezone unaware datetime',dt_aTime)
        exit()

    dt_aTime=dt_aTime.astimezone(pytz.timezone('US/Eastern'))    
    if dt_aTime.weekday()==6 or dt_aTime.weekday()==5:
        #print 'weekend'
        if version=='true_or_false':        
            return False
        else:
            return None
    if dt_aTime.date() in holiday:
        #print 'holiday'
        if version=='true_or_false':        
            return False
        else:
            return None
            
    if dt_aTime.date() in earlyClosing:
        marketStartTime=dt_aTime.replace(hour=int(start.split(':')[0]), minute=int(start.split(':')[1]), second=0)
        marketCloseTime=dt_aTime.replace(hour=int(early_end.split(':')[0]), minute=int(early_end.split(':')[1]), second=0)
    else:
        marketStartTime=dt_aTime.replace(hour=int(start.split(':')[0]), minute=int(start.split(':')[1]), second=0)
        marketCloseTime=dt_aTime.replace(hour=int(end.split(':')[0]), minute=int(end.split(':')[1]), second=0)

    if version=='market_close_time':
        return marketCloseTime
    elif version=='market_open_time':
        return marketStartTime
    elif version=='true_or_false':       
        if dt_aTime>marketStartTime and dt_aTime<=marketCloseTime:
            #print marketStartTime.strftime(fmt)
            #print marketCloseTime.strftime(fmt)
            #print 'OPEN '+dt_aTime.strftime(fmt)   
            return True
        else:
            #print marketStartTime.strftime(fmt)
            #print marketCloseTime.strftime(fmt)
            #print 'CLOSE '+dt_aTime.strftime(fmt)      
            return False
    else:
        print ('small_tools::if_market_is_open: EXIT, Cannot handle version=',version)
        exit()

def market_time(dt_aTime, version):
    if dt_aTime.tzinfo==None:
        print ('small_tools::market_time: cannot handle timezone unaware datetime',dt_aTime)
        exit()
    if version=='open_time':    
        tp=if_market_is_open(dt_aTime, version='market_open_time')
    elif version=='close_time':
        tp=if_market_is_open(dt_aTime, version='market_close_time')
    else:
        print ('small_tools::market_time: EXIT, Cannot handle version=',version)
        exit()
        
    if tp==None:
        print ('market is closed today',dt_aTime)
        return None
    else:
        return tp
 
def add_realtimeBar_to_hist(data, sec, hist_frame):
    data[sec].hist[hist_frame]=data[sec].hist[hist_frame].drop(data[sec].hist[hist_frame].index[-1]) #remove the last line, potential uncompleted data
    #print data[context.sec].hist[hist_frame].tail()
    #print data[context.sec].realTimeBars
      
    tmp= pd.DataFrame(data[sec].realTimeBars, columns=['sysTime','datetime', 'open', 'high', 'low', 'close', 'volume', 'wap', 'count'])
    tmp['datetime']=tmp['datetime'].apply(lambda x: dt.datetime.fromtimestamp(x))    
    tmp=tmp.set_index('datetime')
    tmp=tmp.resample('30s',how={'open':'first','high':'max','low':'min','close':'last', 'volume':'sum'} )

    for idx in tmp.index:
        if idx in data[sec].hist[hist_frame].index:
            #print 'drop',idx
            tmp=tmp.drop(idx)
        else:
            break
    #print tmp
    if len(tmp)>=1:
        data[sec].hist[hist_frame]=data[sec].hist[hist_frame].append(tmp)
    #print data[context.sec].hist[hist_frame].tail()
    if len(data[sec].hist[hist_frame])>100:
        data[sec].hist[hist_frame]=data[sec].hist[hist_frame].drop(data[sec].hist[hist_frame].index[0])

def rounding(num, rounding=0.01):
    if rounding!=0:
        return int(num/rounding)*rounding
    else:
        return int(num)

def _match(target, val, version):
    if target=='any':
        return True
    else:
        if version=='monthWeek':
            if target>=0:
                return target==val[0]
            else:
                return target==val[1]
        elif version=='hourMinute':
            return target==val
        else:
            print (__name__+'::_match: EXIT, cannot handle version=%s'%(version,))
            exit()    
    
if __name__=='__main__':

    #a=dt.datetime(2017,5,1,9,30)
    #showTimeZone=pytz.timezone('US/Eastern')
    #b=dt_to_utc_in_seconds(a, showTimeZone)
    #print (b)
    #c=dt.datetime.fromtimestamp(b)
    #print (c)
    #print (showTimeZone.localize(c))

    a=dt.datetime(2017,6,14,16,0)
    print (if_market_is_open(pytz.timezone('US/Eastern').localize(a)))