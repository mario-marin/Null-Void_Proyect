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
        server_list = [] #arreglo donde cada indice reŕecenta un servidor, y cada indice contiene informacion de ese servidor (por ahora solo su tasa de atencion, numero de bloqueos y capacidad total)
        for x in range(0,number_of_servers):
            server_list.append([tasa_de_atencion,0,capacity])
            
    def process_load(self): #metodo porsesa al usuario entrante, viendo si es en efecto atendido (ocupando al servidor) o es enviado a una cola    
        
    def attend_user(self): #metodo prosesa el requerimiento del usuario entrante, (generando prob de salida)
        
    def queue_user(self): #el servidor no puede atender al usuario por lo tanto es enviaod a una cola (para probar denuevo)