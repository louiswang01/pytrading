# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 19:01:54 2014

@author: Huapu (Peter) Pan
"""
import os
import datetime
import pytz

Level={
'NOTSET':0, # show more info
'DEBUG' : 10,
'INFO' : 20,
'ERROR' : 30} # show less info

class SimpleLoggerClass(object):
    def __init__(self, filename, logLevel, folderPath='default', addTime=True):
        """ determine US Eastern time zone depending on EST or EDT """
        if datetime.datetime.now(pytz.timezone('US/Eastern')).tzname() == 'EDT':
            self.USeasternTimeZone = pytz.timezone('Etc/GMT+4')
        elif datetime.datetime.now(pytz.timezone('US/Eastern')).tzname() == 'EST':
            self.USeasternTimeZone = pytz.timezone('Etc/GMT+5')   
        else:
            self.USeasternTimeZone = None
        self.addTime = addTime  # True: add local time str in front of the records
        self.filename = filename # User defined fileName
        self._logLevel = Level[logLevel] # 
        if folderPath == 'default':
            self.folderPath = os.path.join(os.getcwd(), 'Log')
        else:
            self.folderPath = folderPath  
        if not os.path.isdir(self.folderPath):
            os.makedirs(self.folderPath)
            print (__name__+'::__init__: WARNING, create a folder of "Log" at %s' %(self.folderPath,))
              
    def _write_to_log(self, msg, verbose=True):
        currentTime = datetime.datetime.now(tz = self.USeasternTimeZone)
        if verbose:
            print (msg)
        self.open_file()
        if self.addTime:
            self._log_file.write(str(currentTime) + ": " + msg + '\n')
        else:
            self._log_file.write(msg + '\n')            
        self.close_log()        

    def notset(self, msg, verbose=True):
        if (self._logLevel <= Level['NOTSET']):
            self._write_to_log(msg, verbose=verbose)

    def debug(self, msg, verbose=True):
        if (self._logLevel <= Level['DEBUG']):
            self._write_to_log(msg, verbose=verbose)
        
    def info(self, msg, verbose=True):
        if (self._logLevel <= Level['INFO']):
            self._write_to_log(msg, verbose=verbose)

    def error(self, msg, verbose=True):
        if (self._logLevel <= Level['ERROR']):
            self._write_to_log(msg, verbose=verbose)
        
    def record(self, *arg, **kwrs):
        msg = ''
        for ct in arg:
            msg += str(ct) + ' '
        for ct in kwrs:
            msg += str(kwrs[ct]) + ' '
        self._write_to_log(msg, verbose=False)
        
    def close_log(self):
        self._log_file.close()
    
    def open_file(self):
        self._log_file = open(os.path.join(self.folderPath, self.filename), 'a') 

if __name__=='__main__':
    #c=  SimpleLoggerClass('TestLog.txt', 'DEBUG', addTime=False) 
    c=  SimpleLoggerClass('TestLog.txt', 'INFO') 
    c.info('test test') 
    c.info('test 1') 
    c.info('test 2', verbose=False) 
    c.info('test 3') 
    c.info('test 4') 
    #c.record(a=1, b=2, c=3)
    c.record(1, 2, 3,'test',1,'retest',4, a=4, b=5, c=6)
    