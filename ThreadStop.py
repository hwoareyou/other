import time
import threading


class DownThread:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)


if __name__ == '__main__':
    c = DownThread()
    t = threading.Thread(target=c.run, args=(10,))
    t.start()
    time.sleep(3)
    c.terminate()
    t.join()