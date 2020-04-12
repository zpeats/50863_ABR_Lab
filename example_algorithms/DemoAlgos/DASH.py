import json
from data_stru import TestInput2,BufferOccupancy


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







def DASH(n=3, T_low=4, T_rich=20, s=1, B_total=TestInput.buffer_occupancy.current, B_cur, T_elapsed,TH_arr,l,T_grace,C_aba,D):
    '''
    Input: 
    n = 3: the number of bandwidth estimation samples (3 for VOD)
    T_low = 4: the threshold for deciding that the buffer length is low
    T_rich = 20: the threshold for deciding that the buffer length is sufficient
    s = 1: the step down factor for decreasing the bitrate when the buffer length is low
    B_total: the total bytes for segment (or chunk) i
    B_cur:  the total received bytes up to now for segment i
    T_elapsed: the elapsed time from the download of first byte for segment i
    TH_arr: the throughput array used in abandon requests rule (in bps)
    l = 5: the minimum length to average the throughput in Abandon requests rule
    T_grace = 0.5: the grace time threshold used in abandon requests rule
    C_aba = 1.8: the constant for the decision of abandoning the segment in abandon requests rule
    D: the segment duration
    '''

