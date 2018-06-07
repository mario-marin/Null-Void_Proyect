'''
Created on 04-06-2018

@author: mario
'''

class scheduler(object): #realizar un scheduler como el de las tareas (el de c) en python
    '''
    classdocs
    '''


    def __init__(self): #los eventos tienen id_evento,id_usuario,tiempo_evento (en ese orden)
        '''
        Constructor
        '''
        self.event_list = []
        
        
    def push_event(self,id_evento,id_usuario,tiempo_evento):
        obj = [[id_evento,id_usuario,tiempo_evento]]
        if len(self.event_list) == 0: 
            self.event_list.append(obj[0])
        else:
            if self.event_list[0][2] > tiempo_evento: #primer elemento
                self.event_list = obj + self.event_list
            else:
                if self.event_list[len(self.event_list)-1][2] < tiempo_evento: #ultimo elemento
                    self.event_list.append(obj[0])    
                else:
                    for x in range(1,len(self.event_list)): #entremedio
                        if self.event_list[x][2] > tiempo_evento: 
                            self.event_list.insert(x,obj[0]) 
                
        print(self.event_list)
        
    def pop_event(self):
        if len(self.event_list) != 0:
            return self.event_list.pop(0)
        else:
            return False
    
    