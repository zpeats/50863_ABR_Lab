import json
from pprint import pprint as pp

from data_stru import TestInput,BufferOccupancy


with open(r'example_algorithms\TestInputs\test_input1.json') as f:
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

# print(data)
# print(TestInput.buffer_occupancy['time'])
# print(TestInput.buffer_occupancy.time)

rate_prev = 0
R_i = TestInput.available_bitrates
# print(list(i[1] for i in R_i if i[1] < rate_prev))
less_rate_prev= list(i[1] for i in R_i if i[1] < rate_prev)
if less_rate_prev == []:
    rate_mins = 0
    
else: 
    rate_mins = max(less_rate_prev)
# rate_mins = max(list(i[1] for i in R_i if i[1] < rate_prev))
print(rate_mins)


# def bufferbased(rate_prev = 0, buf_now=TestInput.buffer_occupancy, r=TestInput.chunk_time+1, cu = 126,R_i = TestInput.available_bitrates):
#     R_max = max(i[1] for i in R_i)
#     R_min = min(i[1] for i in R_i)

#     # R_max = max(R_i[0])
#     # R_min = min(R_i[0])
    
#     if rate_prev == R_max:
#         rate_plus = R_max
#     else:
#         rate_plus = min(i[1] for i in R_i if i[1] > rate_prev)
#         #rate_plus = min{R_i : R_i > rate_prev} #not sure what this is saying exactly
#         # min(i for i in test_list if i > k)
        
#     if rate_prev == R_min:
#         rate_mins = R_min
#     else:
#         rate_mins = max(i[1] for i in R_i if i[1] < rate_prev)
#         #rate_mins = max{R_i : R_i < rate_prev} #not sure what this is saying exactly

#     if buf_now.time <= r:
#         rate_next = R_min
#     elif buf_now.time >= (r + cu):
#         rate_next = R_max
#     elif buf_now.size >= rate_plus:
#         rate_next = max(i[1] for i in R_i if i[1] < buf_now.size)
#         # rate_next = max{R_i : R_i < buf_now.size}
#     elif buf_now.size <= rate_mins:
#         rate_next = min(i[1] for i in R_i if i[1] > buf_now.size)
#         #rate_next = min{R_i : R_i > buf_now.size}
#     else:
#         rate_next = rate_prev
#     return rate_next

# next_rate =bufferbased(rate_prev = 0, buf_now=TestInput.buffer_occupancy, r=TestInput.chunk_time+1, cu = 126,R_i = TestInput.available_bitrates)
# print(next_rate)