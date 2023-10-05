import socket
import matplotlib.pyplot as plot

bind_ip = socket.gethostbyname(socket.gethostname())
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen()

print("Listening on", bind_ip, ":", bind_port)
plot.ion()
fig, ax = plot.subplots(3,4)

while True:
    client, addr = server.accept()
    print ('Connected by', addr)
    d = [[] for _ in range (0, 12)]

    while True:
        data = list(map(float, client.recv(1024).decode('utf-8').split(' ')[:-1]))
        # data = client.recv(1024).decode('utf-8').split(' ')
        print("Client recv data :", data)

        shift = 0
        for i in range(len(data)):
            try:
                d[i - shift].append(data[i])
            except:
                shift += 12
                # print("more than 12 data! Operate a shift! ")
                d[i - shift].append(data[i])
                # print("For debug: i = ", i, ", len(data) = ", len(data), sep = '')
        
        # print("d:", d)
        for i in range(0, 3):
            for j in range(0, 4):
                ax[i][j].clear()
                ax[i][j].plot(d[i*4+j])
        ax[0][0].title.set_text('Temperature')
        ax[0][1].title.set_text('Humidity')
        ax[0][2].title.set_text('Pressure')
        ax[0][3].title.set_text('Magneto_X')
        ax[1][0].title.set_text('Magneto_Y')
        ax[1][1].title.set_text('Magneto_Z')
        ax[1][2].title.set_text('Gyro_X')
        ax[1][3].title.set_text('Gyro_Y')
        ax[2][0].title.set_text('Gyro_Z')
        ax[2][1].title.set_text('Accelero_X')
        ax[2][2].title.set_text('Accelero_Y')
        ax[2][3].title.set_text('Accelero_Z')
        plot.show()
        plot.pause(0.001)

        # client.send("ACK!".encode())
