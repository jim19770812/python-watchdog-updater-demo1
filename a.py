import importlib
import time
import a
import c
import threading

c=importlib.import_module("c")
class A(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self) -> None:
        for i in range(1000):
            importlib.reload(a)
            importlib.reload(c)
            c.hello("A")
            time.sleep(0.3)
