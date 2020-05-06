#Written by Nathan A-M =^)

#Dash Industry Forum Reference Client Algorithm implementation 
#using Practical Eval Paper as a reference 
#Didn't include Abandon request rule used because it seemed overly
#complicated to fit with our system

bitrate = 0 
def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    global bitrate
    R_i = list(Available_Bitrates.items())
    R_i.sort(key=lambda tup: tup[1] , reverse=True)
    bitrate = DASH(buf_time = Buffer_Occupancy['time'], rebuffering = Rebuffering_Time ,est_bandwidth=Measured_Bandwidth, T_low=4, T_rich=20, R_i = R_i, previous_bitrate =bitrate)
    return bitrate

#helper function, to find the corresponding size of bitrate
def match(value, list_of_list): 
    for e in list_of_list:
        if value == e[1]:
            return e
#helper function, return index of bitrate from Available_Bitrates
def index(value,list_of_list):
    for e in range(len(list_of_list)):
        if value == list_of_list[e]:
            return e
    return len(list_of_list)-1

def DASH(buf_time, rebuffering ,est_bandwidth, R_i , previous_bitrate, T_low=4, T_rich=20):
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

    m = len(R_i)
    if buf_time >= T_low*2:
        for k in range(0, m):
            if est_bandwidth/8 >= R_i[k][1]: #get reasonable value under bandwidth
                rate_next = R_i[k][0]
                break
    
    #insufficient buffer rule: 

    if rebuffering != 0: #if there's any rebuffering return lowest possible
        rate_next = R_i[m-1][0]
        return rate_next
    elif T_low < buf_time and buf_time < T_low *2: # if there's buffer time work your way to a good rate
        R_min = match(min(i[1] for i in R_i),R_i)
        i=index(previous_bitrate,R_i)
        if R_min == R_i[i]:
            rate_next = R_i[i][0]
        else:
            rate_next = R_i[i+1][0] 
        return rate_next

    # buffer occupancy rule: 

    if buf_time > T_rich: #if there's a lot of buffer time return the highest possible
        rate_next = R_i[0][0]
        return rate_next
    try:
        return rate_next # return output of throughput rule
    except UnboundLocalError:
        return R_i[m-1][0] #nothing worked, return lowest