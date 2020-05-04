import socket
import json
import time

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6000))

def send_req_json(m_band, prev_throughput, buf_occ, av_bitrates, current_time, chunk_arg, rebuff_time, pref_bitrate ):

    #pack message
    req = json.dumps({"Measured Bandwidth" : m_band,
                     "Previous Throughput" : prev_throughput,
                     "Buffer Occupancy" : buf_occ,
                     "Available Bitrates" : av_bitrates,
                     "Video Time" : current_time,
                     "Chunk" : chunk_arg,
                     "Rebuffering Time" : rebuff_time,
                     "Preferred Bitrate" : pref_bitrate,
                     "exit" : 0})
    req += '\n'

    s.sendall(req.encode())

    message = ""
    while(1):
        messagepart = s.recv(2048).decode()

        #print(messagepart)
        message += messagepart
        if message[-1] == '\n':
            #print(message)

            response = json.loads(message)

            return response["bitrate"]


def send_exit():
    req = json.dumps({"exit" : 1})

    req += '\n'
    s.sendall(req.encode())


if __name__ == "__main__":
    pass