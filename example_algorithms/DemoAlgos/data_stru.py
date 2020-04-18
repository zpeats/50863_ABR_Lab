from typing import Optional, List, Union

class BufferOccupancy:
    current: Optional[int]
    size: int
    time: float
    left: Optional[int]

    def __init__(self, current: Optional[int], size: int, time: float, left: Optional[int]) -> None:
        self.current = current
        self.size = size
        self.time = time
        self.left = left


class TestInput2:
    measured_bandwidth: float
    buffer_occupancy: BufferOccupancy
    available_bitrates: List[List[Union[int, int]]]
    video_time: float
    rebuffering_time: float
    chunk: BufferOccupancy
    previous_bitrate: List[Union[int, str]]
    preferred_bitrate: str

    def __init__(self, measured_bandwidth: float, buffer_occupancy: BufferOccupancy, available_bitrates: List[List[Union[int, str]]], video_time: float, rebuffering_time: float, chunk: BufferOccupancy, previous_bitrate: List[Union[int, str]], preferred_bitrate: str) -> None:
        self.measured_bandwidth = measured_bandwidth
        self.buffer_occupancy = buffer_occupancy
        self.available_bitrates = available_bitrates
        self.video_time = video_time
        self.rebuffering_time = rebuffering_time
        self.chunk = chunk
        self.previous_bitrate = previous_bitrate
        self.preferred_bitrate = preferred_bitrate
