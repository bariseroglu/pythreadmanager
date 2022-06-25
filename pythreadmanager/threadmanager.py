from threading import Thread
import time

class Once:

    def __init__(self, func, args, daemon=False):
        self.func = func
        self.args = args
        self.terminator = False
        self.thread = Thread(target=self.func, args=args, daemon=daemon)
        self.thread.start()

    def wait(self):
        self.thread.join()

class Loop:

    def __init__(self, func, args, timer, daemon=False):
        self.func = func
        self.args = args
        self.timer = timer
        self.terminator = False
        self.thread = Thread(target=self.loop, daemon=daemon)
        self.thread.start()

    def loop(self):
        while True:
            if self.terminator: break
            time.sleep(self.timer)
            self.func(*self.args)

    def wait(self):
        self.thread.join()

    def terminate(self):
        self.terminator = True


class Timeout:

    def __init__(self, func, args, timeout, daemon=False):
        self.func = func
        self.args = args
        self.timeout = timeout
        self.thread = Thread(target=self.timeoutFunc, daemon=daemon)
        self.thread.start()

    def timeoutFunc(self):
        time.sleep(self.timeout)
        self.func(*self.args)

    def wait(self):
        self.thread.join()
