#Written by Nathan A-M =^)
#Hybrid Algorithm implementation using Oboe Paper as a reference 
#Beta parameter fine tuned to handle the worst network conditions

def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    R_i = list(Available_Bitrates.items())
    R_i.sort(key=lambda tup: tup[1] , reverse=True)
    return HYB(B =Previous_Throughput , L = Buffer_Occupancy['current'], R_i = R_i)


def HYB(B, L, R_i,beta =2E-5 ):
    '''
    Input:
    B: throughput from previous values (current bitrate/estimated bandwidth)
    beta:  weight (between 0 and 1) where higher values represent aggressive ABR behavior
    L: Buffer length  
    R_i: Array of bitrates of videos, key will be bitrate, and value will be the byte size of the chunk
    
    Output: 
    Rate_next: The next video rate
    '''

    #Hybrid algorithms
    m = len(R_i)
    threshold = L*beta*(B/8) #get threshold
    for k in range(m):
        if R_i[k][1] <= threshold: #find reasonable value within threshold
            rate_next = R_i[k][0]
            return rate_next
    return R_i[m-1][0]