'''
Created on 04-06-2018

@author: mario
'''

class queue_layer(object):
    '''
    classdocs
    '''


    def __init__(self, numero_de_colas, capacidad_de_colas, tasa_de_abandono, tasa_de_reintento):
        '''
        Constructor
        '''
        queue_list = [] #idea similar eal server_list
        for x in range(0,numero_de_colas):
            queue_list.append([capacidad_de_colas,tasa_de_abandono,tasa_de_reintento,0]) #el 0 final corresponde a el usuao inicial de la cola
    
    def assign_queue(self): #metodo decide a que cola enviar al usuario entrante (enviedo desde el server), si todas las colas estan en la pasta entonses botar la coneccion (bloqueo)
        
    def pop_cola(self,id_cola): #metodo ingresa a el usuario siguiente a el sistema (este usuario debe ser atendido y no puede ser rechazado por el server)
        
    