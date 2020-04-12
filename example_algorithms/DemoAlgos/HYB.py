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
        if value in e:
            return e


def HYB(Sj = TestInput.chunk.size, current_bitrate=TestInput.buffer_occupancy.current, est_bandwidth=TestInput.measured_bandwidth , beta =.000001, L = TestInput.buffer_occupancy.size, R_i = TestInput.available_bitrates):
    '''
    Input:
    Sj: Chuck size
    B: throughput from previous values (current bitrate/estimated bandwidth)
    current_bitrate: 
    est_bandwidth: estimated bandwidth
    beta:  weight (between 0 and 1)
    L: Buffer length/size 
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    
    Output: 
    Rate_next: The next video rate
    '''
    B = current_bitrate/est_bandwidth
    # print(B)
    # print(L)
    m = len(R_i)-1
    threshold = L*beta*B
    # print(threshold)
    for k in range(m):
        if R_i[k][1] <= threshold:
            rate_next = R_i[k][1]
            return rate_next
    



    #return rate_next

next_rate = HYB(Sj = TestInput.chunk.size, current_bitrate=TestInput.buffer_occupancy.current, est_bandwidth=TestInput.measured_bandwidth , beta =.000001, L = TestInput.buffer_occupancy.size, R_i = TestInput.available_bitrates )
print(next_rate)


print(match(next_rate,TestInput.available_bitrates)[0])