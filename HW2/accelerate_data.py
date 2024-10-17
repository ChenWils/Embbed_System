import socket
import json
import numpy as np
import matplotlib.pyplot as plot

HOST = '192.168.50.234' # IP address
PORT = 8000 # Port to listen on (use ports > 1023)

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
print("Starting server at: ", (HOST, PORT))

# 等待客戶端連接
conn, addr = s.accept()
print(f"Connected by {addr}")
remain =[]

while True:
    data = conn.recv(1024).decode('utf-8')
    print("Received from socket server:", data)
    data_new = []
    num= data.count('{')
    buffer_data = data.split('}')

    for i in range(0,num):
        data_t = buffer_data[i] + '}'
        print(data_t)
        obj = json.loads(data_t)
        t = obj['s']
        print( obj['s'])
        print( obj['x'])
        print( obj['y'])
        print( obj['z'])
        plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
        plot.scatter(t, obj['y'], c='red') # x, y, z, gx, gy, gz
        plot.scatter(t, obj['z'], c='cyan') # x, y, z, gx, gy, gz

        plot.xlabel("sample num")
        plot.pause(0.001)

    # if (data.count('}') != 1):
    #     choose = 0
    #     buffer_data = data.split('}')
    #     while buffer_data[choose][0] != '{':
    #         choose += 1
    #     data = buffer_data[choose] + '}'

    # print(data)
    # obj = json.loads(data)
    # t = obj['s']
    # print(t)
    # print(obj['x'])
    # break
    # plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
    # plot.scatter(t, obj['y'], c='red') # x, y, z, gx, gy, gz
    # plot.scatter(t, obj['z'], c='cyan') # x, y, z, gx, gy, gz
           
    # plot.xlabel("sample num")
          
            
            
        
    # plot.pause(0.0001)