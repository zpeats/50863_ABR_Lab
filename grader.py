import os
import subprocess
import threading
import sys

#This file was written by Zach Peats
#This program repeatedly invokes Simulator.py and studentComm.py in order to run multiple testcases autonomously
#For more information check out the readme



def run_student_code():
    subprocess.run(['python', 'studentComm.py'])
    return


if __name__ == "__main__":

    #check for verbosity
    verboseflag = ""
    if "-v" in sys.argv or "--verbose" in sys.argv:
        verboseflag = "-v"

    switch_ratio = 1
    buffer_ratio = 1



    manifestfilename = 'manifest.json'
    tracefilename = 'trace.txt'



    outtext = []

    #iterate over all test directories
    for testdir in os.listdir('./tests/'):


        testpath = "./tests/" + testdir + "/"

        manifestpath = testpath + manifestfilename
        tracepath = testpath + tracefilename

        #Run student process
        student_thread = threading.Thread(target=run_student_code)
        student_thread.start()

        #run simulator process
        output = subprocess.run(['python', 'simulator.py', tracepath, manifestpath, verboseflag], capture_output=True )

        student_thread.join()

        #decode output and come up with a final score

        outputlines = output.stdout.decode('unicode_escape').split('\n')

        sanitizedoutput = [line.strip() for line in outputlines]

        outtext.append(testdir + ": ")
        outtext.append("\n")
        outtext += outputlines
        outtext.append("\n")

        average_bitrate = None
        buffer_time = None
        switches = None

        for line in sanitizedoutput:
            if "Average bitrate" in line:
                average_bitrate = float(line.split(':')[1])

            if "buffer time" in line:
                buffer_time = float(line.split(':')[1])

            if "switches" in line:
                switches = float(line.split(':')[1])

        #check to ensure that diagnostic scores are found
        if switches is not None and buffer_time is not None and average_bitrate is not None:
            buffer_penalty = pow( (1 - (.05 * buffer_ratio)), buffer_time)
            switch_penalty = pow( (1 - (.08 * switch_ratio)), switches)

            score = average_bitrate * buffer_penalty * switch_penalty

            outtext.append("Score:")
            outtext.append(str(score))
            outtext.append('\n')
            outtext.append('\n')
            outtext.append('\n')

        else:
            outtext.append("Unexpected output from the simulator")
            outtext.append('\n')
            outtext.append('\n')


    with open("grade.txt", 'w', encoding='utf-8') as outfile:
        outfile.writelines(outtext)