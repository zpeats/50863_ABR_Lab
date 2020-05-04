# 50863 ABR Lab

## Computer Network System: Automatic Bitrate (ABR) Algorithm

Python implementation of a video simulator that request bitrate from a ABR Algorithm

## Description

The objective of this project is to explore the design and implementation of different adaptive bitrate (ABR) algorithms for video streaming. The video simulator within this repository will simulate video download and playback, and continuously prompt a user-written algorithm for bitrate decisions. The entrypoint to the algorithm is ```student_entrypoint``` found in ```studentcodeEX.py```. From there, you are able to implement however you please, wether it be additional classes, preserved state, or other standard libraries. A few example implementations using various ABR algorithms were written, they can be found in ```studentEx/```. The algorithm will be then tested over a variety of different simulated network environments, and ultimately be given a final QoE score as an indicator of how well it performed from a "user point of view".

## Usage

### Testing Custom Cases

After writing an ABR algorithm it can be tested by running ``` studentComm.py ``` in one terminal window and then ``` simulator.py <tracefile.txt> <manifestfile.json> ``` in another. ``` studentComm.py ``` is a simple communication layer between the simulator and the student code inside of ```studentcodeEX.py```. Test conditions can be manipulated by modifying the ``` tracefile.txt ``` and  ``` manifestfile.json ``` files. Their specifications are detailed below.

For example, from the main directory of this repository:

```bash
python studentComm.py
```

```bash
python simulator.py inputs/traceHD.txt inputs/manifestHD.json
```

Where traceHD would give you the bandwidth trace that is suitable for HD and manifestHD would give you the manifest with the other parameters that are suitable for HD. Using a proper ABR algorithm such as HYB would output the highest possible bitrate. Input files found in the ``` inputs/ ``` folder with PQ in their name, will give the ABR algorithm Poor Quality parameters. This will result in a lot of rebuffering and should output the lowest possible bitrate. Manifest Files ending with a P features a user preference which can be used in the ABR algorithm.

#### Demo

![HD Example](https://github.com/zpeats/50863_ABR_Lab/blob/ABR/readmelinks/demo.gif "HD Example")

### Creating Cases

#### Trace

The trace file dictates the bandwidth throughout a test run. On each line the 1st value represents the Video Time threshold where a bandwidth switch occurs and the 2nd value represent the bandwidth value it will switch to. The first and second value must be separated by a single space.

For example,

```text
0 1000000
10 5000000
20 2000000
30 800000
40 1000000
50 5000000
```

A tracefile always must have a value for time 0. There can be as many or as few values as needed. The last bandwidth will describe the bandwidth until the test finishes.

#### Manifest

The manifest file dictates other parameters such as chunks information, available bitrate, buffer size, and much more. ```rand_sizes.py``` can be used to quickly change chunk size information. It uses a normal distribution to randomly generate chunk sizes for a more natural test case.

Here is an example configuration for a Manifest file.

```json
{
  "Video_Time": 60,
  "Chunk_Count": 30,
  "Chunk_Time": 2,
  "Buffer_Size": 4000000,
  "Available_Bitrates": [
    500000,
    1000000,
    5000000
  ],
  "Preferred_Bitrate": null,
  "Chunks": {
    "0" : [
62966,
125069,
567114
],

"1" : [
54274,
132844,
578807
],

"2" : [
68388,
116288,
540269
],
.
.
.
"29" : [
62442,
122537,
563240
]
  }
}
```

### Grader

After writing an ABR algorithm in ``` studentcodeEX.py ```, the grader can be ran using:

```bash
python grader.py
```

The end result will output a grader.txt showing how well the ABR algorithm performed across various test cases with a score as well as other metrics. More test cases can be added by following the same file structure of ``` <test_name>/manifest.json ``` and ``` <test_name>/trace.txt ```

```text
testHD:
Results:
Average bitrate:4850000.0
buffer time:0.101
switches:1

Score:4438943.83557622


testHDmanPQtrace:
Results:
Average bitrate:4850000.0
buffer time:1371.2669999999996
switches:1

Score:1.2666149786445896e-24


testPQ:
Results:
Average bitrate:4850000.0
buffer time:1371.2669999999996
switches:1

Score:1.2666149786445896e-24

```

## Debugging

Both  ```grader.py``` and ```simulator.py``` have verbose options to view more information gathered from the simulator. It can be called via ``` -v ```

For example,

```bash
python simulator.py inputs/traceHD.txt inputs/manifestHD.json -v
```

```bash
python grader.py -v
```

In addition feel free to add print statements within your own code to see how the parameters are changing throughout the course of a test run.

### Demo

![HD Example](https://github.com/zpeats/50863_ABR_Lab/blob/ABR/readmelinks/demov.gif "HD Example")

## Information for Developers

## References for ABR Implementations

T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: evidence from a large video streaming service,” in Proceedings of the 2014 ACM conference on SIGCOMM - SIGCOMM ’14, Chicago, Illinois, USA, 2014, pp. 187–198, doi: 10.1145/2619239.2626296.

I. Ayad, Y. Im, E. Keller, and S. Ha, “A Practical Evaluation of Rate Adaptation Algorithms in HTTP-based Adaptive Streaming,” Computer Networks, vol. 133, pp. 90–103, Mar. 2018, doi: 10.1016/j.comnet.2018.01.019.

Z. Akhtar et al., “Oboe: auto-tuning video ABR algorithms to network conditions,” in Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication - SIGCOMM ’18, Budapest, Hungary, 2018, pp. 44–58, doi: 10.1145/3230543.3230558.
