# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 13:49:50 2014

@author: Huapu (Peter) Pan
"""

class FiniteStateClass(object):
    """
    FiniteStateClass define the finite states of the class instance
    self.states is a class instance whose attributes are the allowed states
    use set_states(states.state) to change state
    """
    
    def __init__(self):
        pass
                
    def set_state(self, state):
        if (hasattr(self, state)):
            self._current_state = state
        else:
            raise Exception("no state named %s exists!" % state)
        
    def current_state(self):
        return self._current_state
        
    def is_state(self, state):
        return self._current_state == state
        
if __name__ == "__main__":
    class TestStateClass(FiniteStateClass):
        def __init__(self):
            self.a = 'a'; self.b = 'b'
    t = TestStateClass()
    t.set_state(t.a)
    print (t.is_state(t.a))
    t.c = "fad"
    
