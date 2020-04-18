'''
Input to the function will be:
{
    "Measured Bandwidth" : float, //the current measured bandwidth, this does not neccessarily mean the bandwidth will stay the same in the future, it's just the current measurement
    "Buffer Occupancy" : {
        "current" : int, //number of bytes occupied in the buffer
        "size" : int, //max buffer size
        "time" : float, //how much video time the occupied buffer represents
        }, 
    "Available Bitrates" : { 
        <string, int> //dynamically packed, key will be bitrate, and value will be the byte size of the chunk. See example below
        //EXAMPLE: "1440" : 20000000
    },
    "Video Time" : float, //current simulated time that has elapsed since start of video. This includes buffering
    "Rebuffing Flag": Boolean, // flag stating that was rebuffing from last bitrate decision
    "Rebuffering Time" : float, //amount of time spent buffering since last request
    "Chunk" : {
        "left" : int, ///number of chunks left in video
        "size" : int, //the total bytes for chunk (or segment) 
        "time": float, //number of second of video next chunk represents  
        }
    "Previous Bitrate" //["0",0] if there was was no previous, same as suggested bitrate
    "Preferred Bitrate " //Bitrate selected by user 

}

Output:
{
    "Chosen Bitrate" : string //Chosen bitrate. Must be one of the keys from "Available Bitrates" in input
}


Feel free to comment/change if there are formats that make more sense

'''






if __name__ == "__main__":
    pass