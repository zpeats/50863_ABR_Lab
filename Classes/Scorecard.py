
#this file was written by Zach Peats
#A class that logs chunk decisions, bitrate switches, and rebuffers

class Scorecard:

    def __init__(self, qual_coef, buf_coef, switch_coef):

        self.qual = qual_coef
        self.buf = buf_coef
        self.switch = switch_coef

        self.rebuffers = []
        self.switches = []
        self.chunk_info = []


    def log_bitrate_choice(self, time, chunknum, chunk):
        self.chunk_info.append({"number" : chunknum,
                                     "time" : time,
                                     "chunk" : chunk})

        self.switching_check()


    def log_rebuffer(self, time, buffer_length):
        if buffer_length == 0:
            return
        self.rebuffers.append((time,buffer_length))

    def switching_check(self):
        if len(self.chunk_info) > 1:
            if self.chunk_info[-1]["chunk"][0] != self.chunk_info[-2]["chunk"][0]:
                self.switches.append({"time" : self.chunk_info[-1]["time"],
                                      "prev_br" : self.chunk_info[-2]["chunk"][0],
                                      "post_br" : self.chunk_info[-1]["chunk"][0]})

    def get_buffer_time(self):
        total = 0
        for rebuffer in self.rebuffers:
            total += rebuffer[1]

        return total

    def get_avg_quality(self):
        total = 0
        for chunk in self.chunk_info:
            total += int(chunk["chunk"][0])

        avg = total / len(self.chunk_info)
        return avg

    def output_results(self):

        print("Results:")
        avg_quality = self.get_avg_quality()
        print("Average bitrate:" + str(avg_quality))

        total_time = self.get_buffer_time()
        print("buffer time:" + str(total_time))

        num_switches = len(self.switches)
        print("switches:" + str(num_switches))


    def output_verbose(self):

        print("Chunk info:")
        for chunk in self.chunk_info:
            print("number: " + str(chunk['number']) + ", time chosen :" + str(chunk["time"]) + ", bitrate: " + str(chunk["chunk"][0]) + ", actual size: " + str(chunk['chunk'][1]))

        print("")
        print("Buffer info:")
        for rebuffer in self.rebuffers:
            print("begin time: " + str(rebuffer[0]), ", length: " + str(rebuffer[1]))

        print("")
        print("Switch info:")
        for switch in self.switches:
            print("time chosen: " + str(switch["time"]) + ", previous bitrate: " + str(switch["prev_br"]) + ", new bitrate: "+ str(switch["post_br"]))

        print("")
        self.output_results()