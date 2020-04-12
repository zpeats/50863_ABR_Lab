import json
from data_stru import TestInput,BufferOccupancy


with open(r'example_algorithms\TestInputs\test_input2.json') as f:
  data = json.load(f)

BufferOccupancy = BufferOccupancy(
    current = data['Buffer Occupancy']['current'],
    size = data['Buffer Occupancy']['size'],
    time = data['Buffer Occupancy']['time']
)

TestInput = TestInput(
    measured_bandwidth=data['Measured Bandwidth'],
    buffer_occupancy = BufferOccupancy,
    chunk_time = data['Chunk Time'] ,
    available_bitrates = data['Available Bitrates'], 
    video_time = data['Video Time'],  
    chunks_remaining= data['Chunks Remaining'],
    rebuffering_time = data['Rebuffering Time'] 
    )

# #print(data)
# #print(TestInput.buffer_occupancy['time'])
# #print(TestInput.buffer_occupancy.time)

def bufferbased(rate_prev = 0, buf_now=TestInput.buffer_occupancy, r=TestInput.chunk_time+1, cu = 126,R_i = TestInput.available_bitrates):
    R_max = max(i[1] for i in R_i)
    R_min = min(i[1] for i in R_i)

    
    #set rate_plus to lowest resonable rate
    if rate_prev == R_max:
        rate_plus = R_max
    else:
        more_rate_prev = list(i[1] for i in R_i if i[1] > rate_prev)
        if more_rate_prev == []:
            rate_plus = 0
        else: 
            rate_plus = max(more_rate_prev)
    #set rate_min to highest resonable rate
    if rate_prev == R_min:
        rate_mins = R_min
    else:
        less_rate_prev= list(i[1] for i in R_i if i[1] < rate_prev)
        if less_rate_prev == []:
            rate_mins = 0
        else: 
            rate_mins = max(less_rate_prev)
    #Buffer based
    if buf_now.time <= r:
        rate_next = R_min
        #print(rate_next)
        #print('^1st')
    elif buf_now.time >= (r + cu):
        rate_next = R_max
        #print(rate_next)
        #print('^2nd')
    elif buf_now.size >= rate_plus:
        less_buff_now= list(i[1] for i in R_i if i[1] < buf_now.current)
        if less_buff_now == []:
            rate_next = 0
        else: 
            rate_next = max(less_buff_now)
        #print(rate_next)
        #print('^3rd')
    elif buf_now.size <= rate_mins:
        more_buff_now= list(i[1] for i in R_i if i[1] > buf_now.current)
        if more_buff_now == []:
            rate_next = 0
        else: 
            rate_next = min(more_buff_now)
        #print(rate_next)
        #print('^4th')
    else:
        rate_next = rate_prev

        #print(rate_next)
        #print('^last')
    return rate_next

next_rate =bufferbased(rate_prev = 0, buf_now=TestInput.buffer_occupancy, r=TestInput.chunk_time+1, cu = 126,R_i = TestInput.available_bitrates)
print(next_rate)
#print('^true')