#Written by Nathan A-M =^)
#Buffer-based implementation using 
#A Buffer-based approach as a reference 

bitrate = 0 #used to save previous bitrate

def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    global bitrate
    R_i = list(Available_Bitrates.items())
    R_i.sort(key=lambda tup: tup[1] , reverse=True)
    bitrate = bufferbased(rate_prev=bitrate, buf_now= Buffer_Occupancy, r=Chunk['time']+1,R_i= R_i ) 
    return bitrate

#helper function, to find the corresponding size of previous bitrate
def match(value, list_of_list): 
    for e in list_of_list:
        if value == e[1]:
            return e
            
#helper function, to find the corresponding size of previous bitrate
#if there's was no previous assume that it was the highest possible value
def prevmatch(value, list_of_list): 
    for e in list_of_list:
        if value == e[1]:
            return e
    value = max(i[1] for i in list_of_list)
    for e in list_of_list:
        if value == e[1]:
            return e

def bufferbased(rate_prev, buf_now, r, R_i , cu = 126):
    '''
    Input: 
    rate_prev: The previously used video rate
    Buf_now: The current buffer occupancy 
    r: The size of reservoir  //At least greater than Chunk Time
    cu: The size of cushion //between 90 to 216, paper used 126
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    
    Output: 
    Rate_next: The next video rate
    '''
    
    R_max = max(i[1] for i in R_i)
    R_min = min(i[1] for i in R_i)
    rate_prev = prevmatch(rate_prev,R_i)
    
    #set rate_plus to lowest reasonable rate
    if rate_prev[1] == R_max:
        rate_plus = R_max
    else:
        more_rate_prev = list(i[1] for i in R_i if i[1] > rate_prev[1])
        if more_rate_prev == []:
            rate_plus = rate_prev[1]
        else: 
            rate_plus = min(more_rate_prev)
    
    #set rate_min to highest reasonable rate
    if rate_prev[1] == R_min:
        rate_mins = R_min
    else:
        less_rate_prev= list(i[1] for i in R_i if i[1] < rate_prev[1])
        if less_rate_prev == []:
            rate_mins = rate_prev[1]
        else: 
            rate_mins = max(less_rate_prev)
    
    #Buffer based Algorithm 
    if buf_now['time'] <= r: #1st check if buffer time is too small, set to R_min
        rate_next = R_min
        rate_next = match(R_min, R_i)[0]
    elif buf_now['time'] >= (r + cu):  #too big, set R_max
        rate_next = R_max
        rate_next = match(R_max, R_i)[0]
    elif buf_now['current'] >= rate_plus: #check if big enough get a different reasonable rate
        less_buff_now= list(i[1] for i in R_i if i[1] < buf_now['current'])
        if less_buff_now == []:
            rate_next = rate_prev[0]
        else: 
            rate_next = max(less_buff_now)
            rate_next = match(rate_next, R_i)[0]
    elif buf_now['current'] <= rate_mins: #check if small enough for a different reasonable rate
        more_buff_now= list(i[1] for i in R_i if i[1] > buf_now['current'])
        if more_buff_now == []:
            rate_next = rate_prev[0]
        else: 
            rate_next = min(more_buff_now)
            rate_next = match(rate_next, R_i)[0]
    else:
        rate_next = rate_prev[0] #else give up and try again next time

    return rate_next