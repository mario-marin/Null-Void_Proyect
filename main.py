'''
Created on 04-06-2018

@author: mario este es el simulador (core)
'''
from scheduler import scheduler
import not_porn
import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        not_porn.beautiful_thig(sys.argv[1])
    
    events = scheduler() 
    events.push_event(10, 10)
    events.push_event(11, 15)
    events.push_event(11, 9)
    events.push_event(20, 100)
    events.push_event(1, 25)
    events.push_event(5, 26)
    
    for x in range(0,15):
        print(events.pop_event())
    
    
    pass