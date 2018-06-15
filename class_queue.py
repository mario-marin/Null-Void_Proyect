'''
Created on 04-06-2018

@author: mario
'''

import numpy
import random

class queue_layer(object):
    '''
    classdocs
    '''


    def __init__(self, numero_de_colas, capacidad_de_colas, tasa_de_abandono):
        '''
        Constructor
        
        '''
        self.numero_de_colas = numero_de_colas
        self.tasa_de_abandono = tasa_de_abandono
        self.queue_list = [] #idea similar eal server_list
        for x in range(0,numero_de_colas):
            self.queue_list.append([capacidad_de_colas,0,[]]) #el 0 es el uso inicial de la cola, por otro lado el arreglo final corresponde a los tiempos de abandono de cada usuario en la cola
    
    def select_queue(self): #metodo decide a que cola enviar al usuario entrante (enviedo desde el server), si todas las colas estan en la pasta entonses botar la coneccion (bloqueo)
        return random.choice(range(0,self.numero_de_colas))
    
    def select_queue_2(self,queue_state): #este metodo entrega el usuario entrante a uno de los servidores por medio de algun criterio (puede ser random)
        if len(queue_state) == 0: # da lo mismo cual escojer por q estan todos cagados
            return random.choice(range(0,self.numero_de_colas))
        else:
            return random.choice(queue_state)
        
    def queue_full_query(self,queue_id):
        if self.queue_list[queue_id][0] <= self.queue_list[queue_id][1]: #si la capacidad es mayor al uso
            return True
        else:
            return False
        
    def queue_empty(self,queue_id):
        if len(self.queue_list[queue_id][2]) == 0:
            return True
        else:
            return False
        
    def not_empty_queue_list(self):
        
        not_empty_queue = list(range(0,self.numero_de_colas))
        
        for queue_id in range(0,self.numero_de_colas):
            if self.queue_list[queue_id][1] == 0:
                not_empty_queue.remove(queue_id)
        return not_empty_queue    
    
        
    def add_to_queue(self,queue_id,sim_time):
        desertion_time = numpy.random.exponential(self.tasa_de_abandono) + sim_time
        self.queue_list[queue_id][1] = self.queue_list[queue_id][1] + 1
        self.queue_list[queue_id][2].append(desertion_time)
        self.queue_list[queue_id][2].sort()
        print("added to queue")
        
    def pop_queue(self,queue_id): #metodo ingresa a el usuario siguiente a el sistema (este usuario debe ser atendido y no puede ser rechazado por el server)
        self.queue_list[queue_id][1] = self.queue_list[queue_id][1] - 1
        print(self.queue_list[queue_id][2].pop(0))
        
    def update_queue(self,sim_time):
        
        for x in range(0,len(self.queue_list)):
            index = 0
            for i in range(0,len(self.queue_list[x][2])):
                if self.queue_list[x][2][i] < sim_time:
                    index = index + 1
                else:
                    break
            while index != 0:
                index  = index - 1
                self.queue_list[x][1] = self.queue_list[x][1] - 1
                self.queue_list[x][2].pop(0)
    
        