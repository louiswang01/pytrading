# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 11:01:38 2014

@author: peter
"""

class PrintableClass(object):
    def __init__(self):
        pass
    
    def print_obj(self):
        t = self.__dict__
        for it in t:
#            print dir(t[it]), hasattr(t[it], 'print_obj')
            if (hasattr(t[it], 'print_obj')):
                t[it].print_obj()
            else:
                print (it, ': ', t[it], '\n')