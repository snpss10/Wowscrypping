import subprocess as sp
import platform
import time
host = '8.8.8.8'




def ping(host):

    #named_tuple = time.localtime()  # get struct_time
    #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    #param = '--n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', '-t',host]

    salida = sp.call(command)
    return salida



print(ping(host))
