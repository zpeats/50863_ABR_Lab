import os
import subprocess
import threading
import sys




def run_student_code():
    subprocess.run(['python', 'studentComm.py'])
    return


if __name__ == "__main__":

    #check for verbosity
    verboseflag = ""
    if "-v" in sys.argv or "--verbose" in sys.argv:
        verboseflag = "-v"



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

        outtext.append(testdir + ": ")
        outtext.append("\n")
        outtext.append(output.stdout.decode('unicode_escape'))
        outtext.append("\n")
        outtext.append("\n")

    with open("grade.txt", 'w', encoding='utf-8') as outfile:
        outfile.writelines(outtext)