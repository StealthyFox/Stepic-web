'''
Разработать простейший TCP echo сервер.
Требования
Запускается на IP адресе 0.0.0.0 и TCP порту 2222 
Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
Закрывает соединение при получении сообщения с текстом close﻿
'''
import socket                                                                   
import os

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)                          
s.bind(('0.0.0.0', 2222))                                                       
s.listen(1)
while True:                                                            
        conn, addr = s.accept()                                 
        while True:                                 
                data = conn.recv(1024)                                  
                if not data: break                                      
                conn.send(data)  
                if data == 'close': break
        print('close it')                                               
        conn.close()
