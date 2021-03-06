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
import math
import os
from datetime import datetime



def exp_rand(rate):
    return numpy.random.exponential(1/rate)

def save_results(temp_data, path):
    
    file_time = str(datetime.now())
    file = str(datetime.now())
    file = file.replace(" ", "_")
    file = file.replace(":", "-")
    file = file.replace(".", "-")
    
    if(not os.path.exists(path)):
        os.mkdir(path)
 
    f = open(path + file + ".txt","w+")
    
    lines = ["#timeline created on: "+ file_time + "\n", 
             "Llegadas totales: " + str(temp_data[0]) + "\n",
             "Usuarios bloqueos: " + str(temp_data[1]) + "\n",
             "Usuarios atendidos: " + str(temp_data[2]) + "\n",
             "Tasa de bloqueo: "+ str(temp_data[3]) + "\n",
             "Numero de usuarios que entraron a las colas: " + str(temp_data[5]) + "\n",
             "Numero de usuarios que abandonaron a las colas: " + str(temp_data[6]) + "\n",
             "Numero de usuarios que fueron atendidos desde las colas: " + str(temp_data[7]) + "\n",
             "Probabilidad de abandono: " + str(temp_data[8]) + "\n",
             "Probabilidad de no atencion: " + str(temp_data[9]) + "\n",
             "Probabilidad de blokeo: " + str(temp_data[4]) + "\n"]
            

    f.writelines(lines) 
    f.close()
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        not_porn.beautiful_thig(sys.argv[1])
    else:
        if len(sys.argv) != 4:
            print("Usage: python main.py {tasa de llegada (float)} {tasa de salida(float)} {tasa de abandono(float)}")
            sys.exit(0)
        
        
    arrivals = 0
    
    
    
    '''
    for x in range(0,100):
        print(numpy.random.exponential(1/float(sys.argv[3])))
    '''
    
    #---------------config load block--------------------
    
    [server_caps, queue_caps] = config_loader.load_config("./config.txt")
    events = scheduler() 
    servers = server_layer(server_caps)
    queues = queue_layer(queue_caps, float(sys.argv[3]))
    switch = balancer(len(server_caps))
        
    #-------------------init block-----------------------
    sim_time = 0
    
    alfa = float(sys.argv[1])
    beta = float(sys.argv[2])
    
    events.push_event(1, None, exp_rand(alfa))
    
    #--------------------simulator-----------------------
    
    atendidos = 0
    bloked = 0
    
    z_alfa_2 =  1.96 # 95.0% de confiavilidad
    RE_dato = 0.05 # 5.0% de error
    
    IC = 1000000
    ER = 100
    
    print_flag = 0
    
    while (IC > ER):
        current_event = events.pop_event()
        if current_event[2] != sim_time:
            sim_time = current_event[2]
        
        queues.update_queue(sim_time)

        
        
        if current_event[0] == 1:
            print_flag = print_flag + 1 
            arrivals = arrivals + 1 #se aumenta las llegadas
            server_id = switch.assign_load(servers.available_servers_list_query()) #selecion de server
            events.push_event(1, None, sim_time+exp_rand(alfa)) #nueva llegada
            if servers.server_full_query(server_id): #servidor lleno?
                id_queue = queues.select_queue() #selecionar fila
                if queues.queue_full_query(id_queue): #fila llena?
                    bloked = bloked + 1 #blokeado
                else:
                    queues.add_to_queue(id_queue, sim_time+sim_time) # se agrega a fila
            else:
                servers.increase_usage(server_id) #se atiende al man, aumenta el uso del server
                events.push_event(0, server_id, sim_time+exp_rand(beta)) #se genera salida
        else:
            if len(queues.not_empty_queue_list()) == 0: #las fials estan vacias?
                servers.decrease_usage(current_event[1]) #se disminulle el uso del server
            else:
                id_queue = queues.select_queue_2(queues.not_empty_queue_list()) #se seleciona fila no vacia
                queues.pop_queue(id_queue) #se saca un man de esa fila selecionada
                events.push_event(0, current_event[1], sim_time+exp_rand(beta)) #se agrega salida
            atendidos = atendidos + 1 #aumenta el numero de manes atendidos satisfactoriamente
        prob = (bloked+queues.abandonos)/arrivals
        if prob != 0:
            IC = prob + z_alfa_2 * math.sqrt(prob*(1-prob)/arrivals)
            ER = prob + prob*RE_dato/2.0
        '''
        if(print_flag == 100000):
            print(IC-ER)
            print_flag = 0;
        '''   
    
    print("Llegadas totales: " + str(arrivals))
    print("Usuarios blokeados: " + str(bloked))
    print("Usuarios atendidos: " + str(atendidos))
    print("Tasa de blokeo: "+str(bloked/atendidos))
    print("Numero de usuarios que entraron a las colas: "+ str(queues.llegadas))
    print("Numero de usuarios que abandonaron a las colas: "+ str(queues.abandonos))
    print("Numero de usuarios que fueron atendidos desde las colas: "+ str(queues.atendidos))
    print("Probabilidad de blokeo: "+ str(bloked/arrivals))
    print("Probabilidad de abandono: " +str(queues.abandonos/queues.llegadas))
    print("Probabilidad de no atencion: " +str(prob))
    
    temp_data = [arrivals,bloked,atendidos,bloked/atendidos,bloked/arrivals,queues.llegadas,queues.abandonos,queues.atendidos,queues.abandonos/queues.llegadas,prob]
    save_results(temp_data, "./saved_timelines/")
    
    
    pass