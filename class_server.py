'''
Created on 04-06-2018

@author: mario

'''

class server:
    def __init__(self,capacity):
        self.usage = 0
        self.capacity = int(capacity)

class server_layer(object):
    '''
    classdocs
    '''


    def __init__(self, serverCaps):
        '''
        Constructor
        '''
        self.number_of_servers = len(serverCaps)
        self.server_list = [] #arreglo donde cada indice reŕecenta un servidor, y cada indice contiene informacion de ese servidor (por ahora solo su tasa de atencion, numero de bloqueos y capacidad total)
        for x in serverCaps:
            self.server_list.append(server(x))
       
       
       
    def server_full_query(self,server_id):
        if self.server_list[server_id].capacity <= self.server_list[server_id].usage:
            return True
        else:
            return False  
        
    def available_servers_list_query(self):
        
        available_servers = list(range(0,self.number_of_servers))
        
        for server_id in range(0,self.number_of_servers):
            if self.server_list[server_id].capacity <= self.server_list[server_id].usage:
                available_servers.remove(server_id)
        return available_servers
        
        
    def increase_usage(self,server_id):
        self.server_list[server_id].usage = self.server_list[server_id].usage + 1
            
    def decrease_usage(self,server_id):
        self.server_list[server_id].usage = self.server_list[server_id].usage - 1
    '''
            
    def process_load(self): #metodo porsesa al usuario entrante, viendo si es en efecto atendido (ocupando al servidor) o es enviado a una cola    
        
    def attend_user(self): #metodo prosesa el requerimiento del usuario entrante, (generando prob de salida)
        
    def queue_user(self): #el servidor no puede atender al usuario por lo tanto es enviaod a una cola (para probar denuevo)
    
    '''
    