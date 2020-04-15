
class Scorecard:

    def __init__(self, qual_coef, buf_coef, switch_coef):

        self.qual = qual_coef
        self.buf = buf_coef
        self.switch = switch_coef

        self.rebuffers = []
        self.switches = []
        self.chunk_qualities = []


    def log_bitrate_choice(self, time, chunknum, chunk):
        #todo: autodetect switching
        self.chunk_qualities.append({"number" : chunknum,
                                     "time" : time,
                                     "chunk" : chunk})

        self.switching_check()


    def log_rebuffer(self, time, buffer_length):
        if buffer_length == 0:
            return
        self.rebuffers.append((time,buffer_length))

    def switching_check(self):
        if len(self.chunk_qualities) > 1:
            if self.chunk_qualities[-1]["chunk"][0] != self.chunk_qualities[-2]["chunk"][0]:
                self.switches.append({"time" : self.chunk_qualities[-1]["time"],
                                      "prev_br" : self.chunk_qualities[-2]["chunk"][0],
                                      "post_br" : self.chunk_qualities[-1]["chunk"][0]})
