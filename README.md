# 50863 ABR Lab

## Computer Network System: Automatic Bitrate (ABR) Algorithm

Python implementation of a video simulator that request bitrate from a ABR Algorithm

## Description

The objective of this project is to explore the design and implementation of different adaptive bitrate (ABR) algorithms for video streaming. The video simulator within this repository will simulate video download and playback, and continuously prompt an algorithm written in ``` studentcodeEX.py ``` for bitrate decisions. A few example implementations using various ABR algorithms were written, they can be found in ```studentEx/```. The algorithm will be then tested over a variety of different simulated network environments, and ultimately be given a final QoE score as an indicator of how well it performed from a "user point of view".

## Usage

### Testing Custom Cases

After writing a ABR algorithm in ``` studentcodeEX.py ``` it can be test by running ``` studentComm.py ``` in one terminal window and then ``` simulator.py <tracefile.txt> <manifestfile.json> ``` in another. ``` studentComm.py ``` prepares the the ABR for incoming parameters from the simulator. Any changes to the simulator output parameter can be done by using different ``` tracefile.txt ``` and  ``` manifestfile.json ``` files.

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

### Grader

After writing a ABR algorithm in ``` studentcodeEX.py ```, the grader can be ran.

```bash
python grader.py
```

The end result will output a grader.txt showing how well the ABR algorithm performed across various test cases. More test cases can be added by following the same file structure of ``` <test_name>/manifest.json ``` and ``` <test_name>/trace.txt ```

```text
testHD:
Results:

Average bitrate:4850000.0

buffer time:0.101

switches:1



testHDmanPQtrace:
Results:

Average bitrate:4850000.0

buffer time:1371.2669999999996

switches:1



testPQ:
Results:

Average bitrate:4850000.0

buffer time:1371.2669999999996

switches:1
```

## References for ABR Implementations

T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: evidence from a large video streaming service,” in Proceedings of the 2014 ACM conference on SIGCOMM - SIGCOMM ’14, Chicago, Illinois, USA, 2014, pp. 187–198, doi: 10.1145/2619239.2626296.

I. Ayad, Y. Im, E. Keller, and S. Ha, “A Practical Evaluation of Rate Adaptation Algorithms in HTTP-based Adaptive Streaming,” Computer Networks, vol. 133, pp. 90–103, Mar. 2018, doi: 10.1016/j.comnet.2018.01.019.

Z. Akhtar et al., “Oboe: auto-tuning video ABR algorithms to network conditions,” in Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication - SIGCOMM ’18, Budapest, Hungary, 2018, pp. 44–58, doi: 10.1145/3230543.3230558.
