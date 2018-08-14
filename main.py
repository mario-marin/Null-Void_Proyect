'''
Created on 04-06-2018

@author: mario este es el simulador (core)
'''
from scheduler import scheduler
from class_queue import queue_layer
from class_server import server_layer
from class_balancer import balancer
import config_loader
import not_porn
import sys
import numpy



def exp_rand(rate):
    return numpy.random.exponential(1/rate)




if __name__ == '__main__':
    if len(sys.argv) > 1:
        not_porn.beautiful_thig(sys.argv[1])
    else:
        print("Usage: python main.py {parada}")
        
        
    stop_condition = int(sys.argv[1])
    arrivals = 0
    
    #---------------config load block--------------------
    data = config_loader.load_config()
    events = scheduler() 
    servers = server_layer(data[0][0], data[0][1])
    queues = queue_layer(data[1][0],data[1][1],data[1][2])
    switch = balancer(data[0][0])
        
    #-------------------init block-----------------------
    sim_time = 0
    alfa = 2000 #tasa de arrivos (mientra mas ma rapido) 
    beta = 50  #tasa de salidas
    
    events.push_event(1, None, exp_rand(alfa))
    
    #--------------------simulator-----------------------
    
    atendidos = 0
    bloked = 0
    
    
    while stop_condition > arrivals:
    
        current_event = events.pop_event()
        if current_event[2] != sim_time:
            sim_time = current_event[2]
        
        queues.update_queue(sim_time)
        
        #print(sim_time)
        #print(queues.queue_list[0].list)
        
        
        if current_event[0] == 1:
            arrivals = arrivals + 1 #se aumenta las llegadas
            server_id = switch.assign_load(servers.available_servers_list_query()) #selecion de server
            events.push_event(1, None, sim_time+exp_rand(alfa)) #nueva llegada
            #print("llegada")
            if servers.server_full_query(server_id): #servidor lleno?
                id_queue = queues.select_queue() #selecionar fila
                if queues.queue_full_query(id_queue): #fila llena?
                    bloked = bloked + 1 #blokeado
                    #print("bloked user")
                else:
                    queues.add_to_queue(id_queue, sim_time+sim_time) # se agrega a fila
            else:
                servers.increase_usage(server_id) #se atiende al man, aumenta el uso del server
                events.push_event(0, server_id, sim_time+exp_rand(beta)) #se genera salida
        else:
            #print("salida")
            if len(queues.not_empty_queue_list()) == 0: #las fials estan vacias?
                servers.decrease_usage(current_event[1]) #se disminulle el uso del server
            else:
                id_queue = queues.select_queue_2(queues.not_empty_queue_list()) #se seleciona fila no vacia
                queues.pop_queue(id_queue) #se saca un man de esa fila selecionada
                events.push_event(0, current_event[1], sim_time+exp_rand(beta)) #se agrega salida
            atendidos = atendidos + 1 #aumenta el numero de manes atendidos satisfactoriamente
    
    print("arrivals: " + str(arrivals))
    print("bloked: " + str(bloked))
    print("atendidos: " + str(atendidos))
    print("Tasa de blokeo: "+str(bloked/atendidos))
    print("Probabilidad de blokeo: "+ str(bloked/arrivals))
    pass