import json
from data_stru import TestInput2,BufferOccupancy


with open(r'example_algorithms\TestInputs\test_input2.json') as f:
  data = json.load(f)

Buffer= BufferOccupancy(
    current = data['Buffer Occupancy']['current'],
    size = data['Buffer Occupancy']['size'],
    time = data['Buffer Occupancy']['time'],
    left = None 
)
Chunk = BufferOccupancy(
    current = data['Chunk']['current'],
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

def DASH(buffer_len = TestInput.buffer_occupancy.size, rebuffering = TestInput.rebuffing_flag ,est_bandwidth=TestInput.measured_bandwidth, T_low=4, T_rich=20, R_i = TestInput.available_bitrates):
    '''
    Input: 
    T_low = 4: the threshold for deciding that the buffer length is low
    T_rich = 20: the threshold for deciding that the buffer length is sufficient
    buffer_len: buffer length 
    est_bandwidth: estimated bandwidth
    rebuffering: flag stating that was rebuffing from last bitrate decision
    buf_now: number of bytes occupied in the buffer
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    
    Output: 
    Rate_next: The next video rate
    '''
    #throughput rule:
    m = len(R_i)-1
    if buffer_len >= T_low*2:
        for k in range(0, m):
            if est_bandwidth >= R_i[k][1]:
                rate_next = R_i[k][1]
                break
    # print(rate_next)
    # print('^1st')
    
    #insufficient buffer rule: 
    if rebuffering:
        rate_next = R_i[m][1]
    elif T_low < buffer_len and buffer_len < T_low *2:
        rate_next = R_i[m][1]
    # print(rate_next)
    # print('^2nd')
    
    # #buffer occupany rule: 
    # if buffer_len > T_rich:
    #     rate_next = R_i[0][1]
    # print(rate_next)
    # print('^last')
    return rate_next


next_rate = DASH(buffer_len = TestInput.buffer_occupancy.size, rebuffering = TestInput.rebuffing_flag ,est_bandwidth=TestInput.measured_bandwidth, T_low=4, T_rich=20, R_i = TestInput.available_bitrates)
print(next_rate)

print(match(next_rate,TestInput.available_bitrates)[0])