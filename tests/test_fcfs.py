from src.core.algorithms.fcfs import FCFS
from src.core.process import Process

def test_fcfs_order():
    fcfs = FCFS()
    p1 = Process(1, 1, 10, 0, 50)
    p2 = Process(2, 1, 5, 1, 60)
    fcfs.add_process(p1)
    fcfs.add_process(p2)
    assert fcfs.get_next_process(0) == p1
    assert fcfs.get_next_process(1) == p2