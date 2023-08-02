import time
import c
import threading


class B(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self) -> None:
        for i in range(10000):
            c.hello("B，没有执行reload")
            time.sleep(0.3)
