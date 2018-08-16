'''
Created on 04-06-2018

@author: mario esta wea su proposito es leer el archivo config y extrae los datos para genrar los objetos en el main
'''

class loadStates:
    _STATE_SERVERS = 1
    _STATE_QUEUES = 2

def load_config(path): #leo el archivo y estraigo los numeritos y despues los retorno en una lista [datos_server,datos_queue,balaner-data]
    
    serverCaps = []
    queueCaps = []
    
    __STATE = -1
    
    fileP = open(path, 'r')
    
    for x in fileP:
        if(x.split()[0] == "S"):
            __STATE = loadStates._STATE_SERVERS
            continue
        elif(x.split()[0] == "Q"):
            __STATE = loadStates._STATE_QUEUES
            continue
        
        if(__STATE == loadStates._STATE_SERVERS):
            serverCaps.append(int(x.split()[0]))
        elif(__STATE == loadStates._STATE_QUEUES):
            queueCaps.append(int(x.split()[0]))
            
    return serverCaps, queueCaps 
    
