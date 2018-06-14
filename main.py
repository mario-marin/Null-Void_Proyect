'''
Created on 04-06-2018

@author: mario este es el simulador (core)
'''
from scheduler import scheduler
from class_queue import queue_layer
from class_server import server_layer
from class_balancer import balancer
import not_porn
import sys
import numpy



def exp_rand(beta):
    return numpy.random.exponential(beta)




if __name__ == '__main__':
    if len(sys.argv) > 1:
        not_porn.beautiful_thig(sys.argv[1])
        
    stop_condition = int(sys.argv[1])
    arrivals = 0
        
    '''
    
    events = scheduler() 
    events.push_event(10,1, 10)
    events.push_event(11,1, 15)
    events.push_event(11,1, 9)
    events.push_event(20,1, 100)
    events.push_event(1, 1,25)
    events.push_event(5, 1,26)
    
    for x in range(0,15):
        print(events.pop_event())
        
        
    queue_layer = queue_layer(1,5,100)
    
    for x in range(0,20):
        queue_layer.add_to_queue( 0, 0)
    queue_layer.update_queue( 20)
    print(queue_layer.queue_list[0][2])
    
    for x in range(0,10):
        queue_layer.pop_cola(0)
    '''
    
    #---------------config load block--------------------
        #TODO
    events = scheduler() 
    queues = queue_layer(1,5,100)
    servers = server_layer(2, 10)
    switch = balancer(2)
        
    #-------------------init block-----------------------
    sim_time = 0
    for x in range(0,servers.number_of_servers):
        for i in range(0,servers.capacity):
            events.push_event(1, None, exp_rand(50))
    
    #--------------------simulator-----------------------
    
    atendidos = 0
    bloked = 0
    
    while stop_condition > arrivals:
    
        current_event = events.pop_event()
        print(current_event)
        if current_event[2] != sim_time:
            sim_time = current_event[2]
        
        queues.update_queue(sim_time)
        
        events.push_event(1,None , exp_rand(50))
        
        if current_event[0] == 1:
            arrivals = arrivals + 1
            list_2 = servers.available_servers_list_query()
            server_id = balancer.assign_load(list_2 )
            if servers.server_full_query(server_id):
                id_queue = queues.select_queue()
                if queues.queue_full_query(id_queue):
                    events.push_event(1, None, exp_rand(50))
                    bloked = bloked + 1
                else:
                    queues.add_to_queue(id_queue, sim_time)
            else:
                servers.increase_usage(server_id)
                events.push_event(0, server_id, exp_rand(50))
        else:
            if len(queues.not_empty_queue_list()) != 0:
                servers.decrease_usage(current_event[1])
            else:
                id_queue = queues.select_queue_2(queues.not_empty_queue_list())
                events.push_event(0, current_event[1], exp_rand(50))
            atendidos = atendidos + 1
            events.push_event(1, None, exp_rand(50))
            
    print(bloked/atendidos)
    pass