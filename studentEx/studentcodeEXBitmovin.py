#Written by Nathan A-M =^)

#Bitmovin Algorithm implementation using 
# Practical Eval Paper as a reference 

bitrate = 0 

def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    global bitrate
    R_i = list(Available_Bitrates.items())
    R_i.sort(key=lambda tup: tup[1] , reverse=True)
    bitrate = bitmovin(time =Video_Time , rate_sug =bitrate , rate_pref =Preferred_Bitrate , R_i = R_i, buf_current=Buffer_Occupancy['current']) 
    return bitrate

#helper function, to find the corresponding size of bitrate
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

def bitmovin(time, rate_sug, rate_pref, R_i, buf_current):
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
    s = prevmatch(rate_sug,R_i)
    
    p = prevmatch(rate_pref,R_i)
    if time < 10:
        for k in range(m):
            if R_i[k] == s:  
                rate_next = s[0]
                return rate_next
            if R_i[k][1] <= p[1]:
                rate_next = R_i[k][0]
                return rate_next
        rate_next = R_i[0][0]
        return rate_next
    else:
        #Rate based Switching
        R_min = ['float("inf")',float("inf")] 
        R_max = ['0',0]
        for k in range(m,-1,-1):
            if R_max[1] < R_i[k][1] and R_i[k][1] < buf_current:
                R_max = R_i[k]
            if R_min[1] > R_i[k][1]:
                R_min = R_i[k]
        if R_max[1] > 0:
            rate_next = R_max[0]
        else:
            rate_next = R_min[0]
        return rate_next