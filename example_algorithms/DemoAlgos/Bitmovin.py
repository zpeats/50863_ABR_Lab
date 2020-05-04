#Written by Nathan A-M =^)
import json
from data_stru import TestInput2, BufferOccupancy


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
    chunk = Chunk,
    preferred_bitrate = data["Preferred Bitrate"] 
    )


def match(value, list_of_list): 
    for e in list_of_list:
        if value in e:
            return e


def bitmovin(time =TestInput.video_time , rate_sug =144 , rate_pref =TestInput.preferred_bitrate , R_i = TestInput.available_bitrates, buf_current=TestInput.buffer_occupancy.current):
    '''
    Input: 
    time: the time passed from start (assuming in sec)
    rate_sug: the rate suggested by other switching methods, if at start this is 0p
    rate_pref: the preferred startup rate
    buf_current: number of bytes occupied in the buffer
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    
    Output: 
    Rate_next: The next video rate
    '''
    
    
    #Preferred Startup Switching 
    m = len(R_i)-1
    s = match(rate_sug,R_i)
    
    p = match(rate_pref,R_i)
    # print(time)
    if time < 10:
        for k in range(m):
            # print(R_i[k])
            if R_i[k] == s:  
                rate_next = s[1]
                # print('End 1')
                return rate_next
            if R_i[k][1] <= p[1]:
                rate_next = R_i[k][1]
                # print('End 2')
                return rate_next
        rate_next = R_i[0][1]
        # print('End 3')
        return rate_next
    else:
        #Rate based Switching
        R_min = float("inf")
        R_max = 0
        for k in range(m,0,-1):
            if R_max < R_i[k][1] and R_i[k][1] < buf_current:
                R_max = R_i[k][1]
            if R_min > R_i[k][1]:
                R_min = R_i[k][1]
        if R_max > 0:
            rate_next = R_max
            print(R_max)
        else:
            rate_next = R_min
        # print('End 4')
        return rate_next

# next_rate = bitmovin(time =9 , rate_sug ="720p" , rate_pref ="1080p" , R_i = TestInput.available_bitrates, buf_current=TestInput.buffer_occupancy.current)
next_rate = bitmovin()
print(next_rate)


print(match(next_rate,TestInput.available_bitrates)[0])