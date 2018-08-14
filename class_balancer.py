'''
Created on 04-06-2018

@author: mario
'''

import random

class balancer(object):
    '''
    classdocs
    '''


    def __init__(self, number_of_servers):
        '''
        Constructor
        '''
        self.number_of_servers = int(number_of_servers)
        
    def assign_load(self,servers_state): #este metodo entrega el usuario entrante a uno de los servidores por medio de algun criterio (puede ser random)
        if len(servers_state) == 0: # da lo mismo cual escojer por q estan todos cagados
            return random.choice(range(0,self.number_of_servers))
        else:
            return random.choice(servers_state)
        

        
    