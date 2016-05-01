import socket                                                                   
import os

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)                          
s.bind(('0.0.0.0', 2222))                                                       
#pid  = os.fork()
for i in s.listen(10)                                                                   
        print('next', i)                                                        
        conn, addr = s.accept()                                                 
        while True:                                                             
                data = conn.recv(1024)                                          
                if not data:                                                    
                        break                                                   
                conn.send(data)                                                 
                if data == 'close':
                        break                                       
        conn.close()                                                            
 
