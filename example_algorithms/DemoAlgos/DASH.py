import json
from data_stru import TestInput2,BufferOccupancy


with open(r'example_algorithms\TestInputs\test_input1.json') as f:
  data = json.load(f)

Buffer= BufferOccupancy(
    current = data['Buffer Occupancy']['current'],
    size = data['Buffer Occupancy']['size'],
    time = data['Buffer Occupancy']['time'],
    left = None 
)
Chunk = BufferOccupancy(
    current = None,
    size = data['Chunk']['size'],
    time = data['Chunk']['time'],
    left = data['Chunk']['left'] 
)

TestInput = TestInput2(
    measured_bandwidth=data['Measured Bandwidth'],
    buffer_occupancy = Buffer,
    available_bitrates = data['Available Bitrates'], 
    video_time = data['Video Time'],  
    rebuffering_time = data['Rebuffering Time'],
    rebuffing_flag = data['Rebuffing Flag'], 
    chunk = Chunk,
    previous_bitrate = data["Previous Bitrate"],
    preferred_bitrate = data["Preferred Bitrate"] 
    )


def match(value, list_of_list): 
    for e in list_of_list:
        if value == e[1]:
            return e
def index(value,list_of_list):
    for e in range(len(list_of_list)):
        if value == list_of_list[e]:
            return e
    return len(list_of_list)-1

#buf_current should be buffer current
def DASH(buf_current = TestInput.buffer_occupancy.current, rebuffering = TestInput.rebuffing_flag ,est_bandwidth=TestInput.measured_bandwidth, T_low=4, T_rich=20, R_i = TestInput.available_bitrates, previous_bitrate =TestInput.previous_bitrate):
    '''
    Input: 
    T_low = 4: the threshold for deciding that the buffer length is low
    T_rich = 20: the threshold for deciding that the buffer length is sufficient 
    est_bandwidth: estimated bandwidth
    rebuffering: flag stating that was rebuffing from last bitrate decision
    buf_current: number of bytes occupied in the buffer
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    previous_bitrate:

    Output: 
    Rate_next: The next video rate
    '''
    #throughput rule:
    m = len(R_i)-1
    if buf_current >= T_low*2:
        for k in range(0, m):
            if est_bandwidth >= R_i[k][1]:
                rate_next = R_i[k][1]
                break
    # print(rate_next)
    # print('^1st')
    
    #insufficient buffer rule: 
    if rebuffering:
        rate_next = R_i[m][1]
        # print(rate_next)
    elif T_low < buf_current and buf_current < T_low *2:
        # print(previous_bitrate)
        # print(R_i)
        R_min = match(min(i[1] for i in R_i),R_i)
        # print(R_min)
        i=index(previous_bitrate,R_i)
        if R_min == R_i[i]:
            rate_next = R_i[i][1]
        else:
            rate_next = R_i[i+1][1]    
        # print(i)
        # print(rate_next)
    # print(rate_next)
    # print('^2nd')
    
    # #buffer occupany rule: 
    if buf_current > T_rich:
        rate_next = R_i[0][1]
    # print(rate_next)
    # print('^last')
    return rate_next


next_rate = DASH()
print(next_rate)

print(match(next_rate,TestInput.available_bitrates)[0])