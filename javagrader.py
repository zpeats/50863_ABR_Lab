import os
import subprocess
import threading
import sys




def run_student_code():
    subprocess.run(['java', '-cp', './javasrc/json-simple-1.1.1.jar;./javasrc/', 'StudentComm'])
    return


if __name__ == "__main__":

    #check for verbosity
    verboseflag = ""
    if "-v" in sys.argv or "--verbose" in sys.argv:
        verboseflag = "-v"

    switch_ratio = 1
    buffer_ratio = 1


    #compile java code
    subprocess.run(['javac', '-cp', './javasrc/json-simple-1.1.1.jar', './javasrc/*.java'], shell=True)

    manifestfilename = 'manifest.json'
    tracefilename = 'trace.txt'



    outtext = []

    for testdir in os.listdir('./tests/'):


        testpath = "./tests/" + testdir + "/"

        manifestpath = testpath + manifestfilename
        tracepath = testpath + tracefilename

        student_thread = threading.Thread(target=run_student_code)
        student_thread.start()


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