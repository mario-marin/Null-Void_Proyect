'''
Created on 04-06-2018

@author: mario
'''

import numpy
import random


class queue:
    def __init__(self,capacidad_de_colas):
        self.capacidad = capacidad_de_colas
        self.usage = 0
        self.list = []


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
        self.llegadas = 0
        self.atendidos = 0
        self.abandonos = 0
        for x in range(0,numero_de_colas):
            self.queue_list.append(queue(capacidad_de_colas)) #el 0 es el uso inicial de la cola, por otro lado el arreglo final corresponde a los tiempos de abandono de cada usuario en la cola
    
    def select_queue(self): #metodo decide a que cola enviar al usuario entrante (enviedo desde el server), si todas las colas estan en la pasta entonses botar la coneccion (bloqueo)
        return random.choice(range(0,self.numero_de_colas))
    
    def select_queue_2(self,queue_state): #este metodo entrega el usuario entrante a uno de los servidores por medio de algun criterio (puede ser random)
        if len(queue_state) == 0: # da lo mismo cual escojer por q estan todos cagados
            return random.choice(range(0,self.numero_de_colas))
        else:
            return random.choice(queue_state)
        
    def queue_full_query(self,queue_id):
        if self.queue_list[queue_id].capacidad <= self.queue_list[queue_id].usage: #si la capacidad es menur al uso
            return True
        else:
            return False
        
    def queue_empty(self,queue_id):
        if len(self.queue_list[queue_id].list) == 0:
            return True
        else:
            return False
        
    def not_empty_queue_list(self):
        
        not_empty_queue = list(range(0,self.numero_de_colas))
        #print(not_empty_queue)
        for queue_id in range(0,self.numero_de_colas):
            #print(queue_id)
            if self.queue_list[queue_id].usage == 0:
                not_empty_queue.remove(queue_id)
        return not_empty_queue    
    
        
    def add_to_queue(self,queue_id,sim_time):
        desertion_time = numpy.random.exponential(1/self.tasa_de_abandono) + sim_time
        self.queue_list[queue_id].usage = self.queue_list[queue_id].usage + 1
        #print(self.queue_list[queue_id].usage )
        self.queue_list[queue_id].list.append(desertion_time)
        self.queue_list[queue_id].list.sort()
        self.llegadas = self.llegadas + 1
        #print("fucker added to queue")
        
    def pop_queue(self,queue_id): #metodo ingresa a el usuario siguiente a el sistema (este usuario debe ser atendido y no puede ser rechazado por el server)
        self.queue_list[queue_id].usage = self.queue_list[queue_id].usage - 1
        #print(self.queue_list[queue_id].list.pop(0))
        self.queue_list[queue_id].list.pop(0)
        self.atendidos = self.atendidos + 1
        
    def update_queue(self,sim_time):
        
        for x in range(0,self.numero_de_colas):
            index = 0
            #print("potato")
            for i in range(0,self.queue_list[x].usage):
                #print("tiempo abandono: " + str(self.queue_list[x].list[i])+"  "+"sim time: "+str(sim_time))
                if self.queue_list[x].list[i] < sim_time: #se miden los que abandonan
                    index = index + 1
                else:
                    break

            while index != 0:
                index  = index - 1
                self.queue_list[x].usage = self.queue_list[x].usage - 1
                #print("tiempo abandono: " + str(self.queue_list[x].list)+"  "+"sim time: "+str(sim_time))
                self.queue_list[x].list.pop(0)
                self.abandonos = self.abandonos + 1
    
        