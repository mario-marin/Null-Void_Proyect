'''
Created on 04-06-2018

@author: mario esta wea su proposito es leer el archivo config y extrae los datos para genrar los objetos en el main
'''



def load_config(): #leo el archivo y estraigo los numeritos y despues los retorno en una lista [datos_server,datos_queue,balaner-data]
    data = []
    config_location = './config.txt'
    
    file_flag = open(config_location,'r')
    
    for x in file_flag.readlines():
        data.append([float(i) for i in x.split()])
    return data 
    
