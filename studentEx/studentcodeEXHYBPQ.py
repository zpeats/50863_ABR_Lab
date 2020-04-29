import random

random.seed(None)

def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    R_i = list(Available_Bitrates.items())
    R_i.sort(key=lambda tup: tup[1] , reverse=True)
    return HYB(buffer_time =Buffer_Occupancy['time'],B =Previous_Throughput  ,est_bandwidth=Measured_Bandwidth, L = Buffer_Occupancy['current'], R_i = R_i)
    # return random_choice(Available_Bitrates)
    #pass

def random_choice(bitrates):
    bitrates_list = [(key, value) for key, value in bitrates.items()]
    choiceind = random.randrange(1, len(bitrates))
    return bitrates_list[choiceind - 1][0]


def HYB(buffer_time, B ,est_bandwidth, L, R_i,beta =2E-5 ):
    '''
    Input:
    B: throughput from previous values (current bitrate/estimated bandwidth)
    buf_now: number of bytes occupied in the buffer
    est_bandwidth: estimated bandwidth
    beta:  weight (between 0 and 1)
    L: Buffer length  
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    buffer_time: how much video time (in secs) the occupied buffer represents 
    
    Output: 
    Rate_next: The next video rate
    '''
    # B = L/buffer_time
    # print(B)
    # print(L)
    # print(beta)
    m = len(R_i)-1
    threshold = L*beta*B
    # print(threshold)
    for k in range(m):
        if R_i[k][1] <= threshold:
            rate_next = R_i[k][0]
            return rate_next
    return R_i[len(R_i)-1][0]