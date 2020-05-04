
#this file was written by Zach Peats
#A class that represents the video playback buffer.

class SimBuffer:

    def __init__(self, bufsize):
        self.size = bufsize
        self.chunks = [] #each chunk object is a tuple (size, chunk_time)
        self.time = 0
        self.cur_size = 0
        self.mid_chunk_time = 0


    def get_student_params(self):
        params = {}
        params["size"] = self.size
        params["current"] = self.cur_size
        params["time"] = self.time
        return params

    def available_space(self):
        #self.buffer_relative_time()
        return self.size - self.cur_size

    def sim_chunk_download(self, chunk_size, chunk_time, playback_time):
        if chunk_size > self.size - self.cur_size:
            print("Error: Chunk being added is too large to fit into buffer")
            return False

        buffer_time = self.sim_playback(playback_time)

        self.chunks.append((chunk_size,chunk_time))
        self.calculate_occupancy()
        self.calculate_time()
        return buffer_time


    def calculate_occupancy(self):
        self.cur_size = 0
        for chunk in self.chunks:
            self.cur_size += chunk[0]

    def burn_time(self, time):
        buffer_time = self.sim_playback(time)
        self.calculate_occupancy()
        self.calculate_time()
        return buffer_time

    def sim_playback(self, playback_time):

        while playback_time > 0:

            #if there are any chunks to be played
            if self.chunks:
                current_chunk = self.chunks.pop(0)

                chunk_time_remaining = current_chunk[1]

                playback_time -= chunk_time_remaining

                if playback_time < 0:
                    chunk_time_remaining = -1 * playback_time
                    self.chunks.insert(0, (current_chunk[0], chunk_time_remaining))
                    return 0


            #no chunks left to be played, buffering
            else:
                return playback_time

        #all playback was simulated, return 0 buffer time
        return 0

    def calculate_time(self):

        totaltime = 0
        for chunk in self.chunks:
            totaltime += chunk[1]

        self.time = totaltime
        return