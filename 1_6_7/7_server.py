'''
Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами. 
'''
import socket                                                                   
import os

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)                          
s.bind(('0.0.0.0', 2222))                                                       
for i in range(10):
        pid = os.fork()
        if pid ==0:
                s.listen(1)
                conn, addr = s.accept()                                 
                print ('neeew', addr) 
                data = conn.recv(1024)
                if not data: break                                      
                print('data is', data)                                  
                conn.send(data)                                         
                print('close it')                                               
                conn.close()
