import socket
import json
import studentcodeEX

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 6000))
ss.listen(10)
print('Waiting for simulator')

(clientsocket, address) = ss.accept()


def recv_commands():
    message = ""


    while(1):
        messagepart = clientsocket.recv(2048).decode()

        #print(messagepart)
        message += messagepart
        if message[-1] == '\n':
            # print(message) #comment out in master

            jsonargs = json.loads(messagepart)
            message = ""

            if(jsonargs["exit"] != 0):
                return

            #todo: json data sanitization
            bitrate = studentcodeEX.student_entrypoint(jsonargs["Measured Bandwidth"], jsonargs["Previous Throughput"], jsonargs["Buffer Occupancy"], jsonargs["Available Bitrates"], jsonargs["Video Time"], jsonargs["Chunk"], jsonargs["Rebuffering Time"], jsonargs["Preferred Bitrate"])

            payload = json.dumps({"bitrate" : bitrate}) + '\n'
            clientsocket.sendall(payload.encode())







if __name__ == "__main__":

    recv_commands()
    ss.close()