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
    print(events.pop_event())
    events.push_event(10, 1, 10)
    events.push_event(11, 1, 15)
    events.push_event(11, 2, 9)
    events.push_event(20, 4, 100)
    events.push_event(1, 4, 25)
    events.push_event(5, 5, 26)
    
    for x in range(0,15):
        print(events.pop_event())
    
    
    pass