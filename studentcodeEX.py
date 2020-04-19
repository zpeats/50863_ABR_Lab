import random

random.seed(None)

def student_entrypoint(Measured_Bandwidth, Previous_Throughput, Buffer_Occupancy, Available_Bitrates, Video_Time, Chunk, Rebuffering_Time, Preferred_Bitrate ):
    #student can do whatever they want from here going forward
    
    return random_choice(Available_Bitrates)

def random_choice(bitrates):
    bitrates_list = [(key, value) for key, value in bitrates.items()]
    choiceind = random.randrange(1, len(bitrates))
    return bitrates_list[choiceind - 1][0]