from typing import List

class BufferOccupancy:
    current: int
    size: int
    time: float

    def __init__(self, current: int, size: int, time: float) -> None:
        self.current = current
        self.size = size
        self.time = time


class TestInput:
    measured_bandwidth: float
    buffer_occupancy: BufferOccupancy
    chunk_time: float
    available_bitrates: List[List[int]]
    video_time: str
    chunks_remaining: str
    rebuffering_time: str

    def __init__(self, measured_bandwidth: float, buffer_occupancy: BufferOccupancy, chunk_time: float, available_bitrates: List[List[int]], video_time: str, chunks_remaining: str, rebuffering_time: str) -> None:
        self.measured_bandwidth = measured_bandwidth
        self.buffer_occupancy = buffer_occupancy
        self.chunk_time = chunk_time
        self.available_bitrates = available_bitrates
        self.video_time = video_time
        self.chunks_remaining = chunks_remaining
        self.rebuffering_time = rebuffering_time