'''
Created on 04-06-2018

@author: mario
'''

class server_layer(object):
    '''
    classdocs
    '''


    def __init__(self, number_of_servers, tasa_de_atencion, capacity):
        '''
        Constructor
        '''
        self.server_list = [] #arreglo donde cada indice reŕecenta un servidor, y cada indice contiene informacion de ese servidor (por ahora solo su tasa de atencion, numero de bloqueos y capacidad total)
        for x in range(0,number_of_servers):
            self.server_list.append([tasa_de_atencion,0,capacity])
       
       
       
    def server_full_query(self,server_id):
        if self.server_list[server_id][2] <= self.server_list[server_id][1]:
            return True
        else:
            return False  
        
    def available_servers_list_query(self):
        
        available_servers = range(0,len(self.server_list))
        
        for server_id in range(0,len(self.server_list)):
            if self.server_list[server_id][2] <= self.server_list[server_id][1]:
                available_servers.remove(server_id)
        return available_servers
        
        
    def increase_usage(self,server_id):
        self.server_list[server_id][1] = self.server_list[server_id][1] + 1
            
    def decrease_usage(self,server_id):
        self.server_list[server_id][1] = self.server_list[server_id][1] - 1
    '''
            
    def process_load(self): #metodo porsesa al usuario entrante, viendo si es en efecto atendido (ocupando al servidor) o es enviado a una cola    
        
    def attend_user(self): #metodo prosesa el requerimiento del usuario entrante, (generando prob de salida)
        
    def queue_user(self): #el servidor no puede atender al usuario por lo tanto es enviaod a una cola (para probar denuevo)
    
    '''
    