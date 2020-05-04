import math

#this file was written by Zach Peats
#A class used to simulate network traces

class NetworkTrace:


    def __init__(self, bandwidths):

        self.bwlist = bandwidths

    #returns the timesegment the time argument is within
    def get_current_timesegment(self, cur_time):
        return min(self.bwlist, key= lambda x: abs(x[0] - cur_time) if cur_time > x[0] else math.inf )


    def simulate_download_from_time(self, time, size):

        cum_time = 0
        timeseg = self.get_current_timesegment(time)

        while(1):
            #find when next bw change is
            next_set = None
            try:
                next_set = self.bwlist[ self.bwlist.index(timeseg) + 1 ]
            except( IndexError ):
                pass

            #if no next bw change, calculate the remaining time
            if not next_set:
                cum_time += size / (timeseg[1] / 8)
                return cum_time

            #find time remaining on current bw, drain download by corresponding amt
            down_time = next_set[0] - time
            cum_time += down_time
            size -= down_time * (timeseg[1] / 8)

            if size <= 0:
                #refund unused time
                unused_time = -1 * size / (timeseg[1] / 8)
                cum_time -= unused_time
                return cum_time

            timeseg = next_set
            time = timeseg[0]

