import json
from data_stru import TestInput2, BufferOccupancy


with open(r'example_algorithms\TestInputs\test_input2.json') as f:
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
    chunk = Chunk,
    preferred_bitrate = data["Preferred Bitrate"] 
    )


def match(value, list_of_list): 
    for e in list_of_list:
        if value in e:
            return e


def HYB(buffer_time = TestInput.buffer_occupancy.time, est_bandwidth=TestInput.measured_bandwidth , beta =.2, L = TestInput.buffer_occupancy.current, R_i = TestInput.available_bitrates):
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
    B = L/buffer_time
    # print(B)
    # print(L)

    m = len(R_i)-1
    threshold = L*beta*B
    # print(threshold)
    for k in range(m):
        if R_i[k][1] <= threshold:
            rate_next = R_i[k][1]
            return rate_next
    return R_i[len(R_i)-1][1]


    #return rate_next

next_rate = HYB()
print(next_rate)


print(match(next_rate,TestInput.available_bitrates)[0])