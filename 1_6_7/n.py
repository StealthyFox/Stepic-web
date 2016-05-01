import socket                                                                   
import os

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)                          
s.bind(('0.0.0.0', 2222))                                                       
s.listen(10)
while True:                                                            
        conn, addr = s.accept()                                 
        print ('neeew', addr)
        pid  = os.fork() 
        if pid == 0:
                data = conn.recv(1024)                                  
                whilel True:
                        if not data: break                                      
                        print('data is', data)                                  
                        conn.send(data)
                        if data == 'close': break
                print('close it')
                conn.close()
