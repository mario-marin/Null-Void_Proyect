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
    alfa = 200
    beta = 50
    
    events.push_event(1, None, exp_rand(alfa))
    
    #--------------------simulator-----------------------
    
    atendidos = 0
    bloked = 0
    
    
    while stop_condition > arrivals:
    
        current_event = events.pop_event()
        #print(current_event)
        if current_event[2] != sim_time:
            sim_time = current_event[2]
        
        queues.update_queue(sim_time)
        
        #events.push_event(1,None , exp_rand(50))
        
        if current_event[0] == 1:
            arrivals = arrivals + 1
            server_id = switch.assign_load(servers.available_servers_list_query() )
            events.push_event(1, None, exp_rand(alfa))
            print("llegada")
            if servers.server_full_query(server_id):
                id_queue = queues.select_queue()
                if queues.queue_full_query(id_queue):
                    bloked = bloked + 1
                    print("bloked user")
                else:
                    queues.add_to_queue(id_queue, sim_time)
            else:
                servers.increase_usage(server_id)
                events.push_event(0, server_id, exp_rand(beta))
        else:
            print("salida")
            if len(queues.not_empty_queue_list()) == 0:
                servers.decrease_usage(current_event[1])
            else:
                id_queue = queues.select_queue_2(queues.not_empty_queue_list())
                queues.pop_queue(id_queue)
                events.push_event(0, current_event[1], exp_rand(beta))
            atendidos = atendidos + 1
    
    print("arrivals: " + str(arrivals))
    print("bloked: " + str(bloked))
    print("atendidos: " + str(atendidos))
    print(bloked/atendidos)
    pass