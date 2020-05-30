
import time
import random
import heapq

from enum import Enum, auto
from threading import Thread


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def rockets():

    N = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]

def launch_rockets(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("rocked launched!")


def run_threads(rockets):
    threads =  [
        Thread(target=launch_rockets, args=(d, c))
        for d, c in rockets
    ]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


class State(Enum):
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()

class Op(Enum):
    WAIT = auto()
    STOP = auto()


class Launch:
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown

    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._delay
        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            print(f"{self._countdown}...")
            self._state = State.WAITING
            self._countdown -=1
            if self._countdown == 0:
                self._state = State.LAUNCHING
            return Op.WAIT, 1

        if self._state is State.LAUNCHING:
            print("Rocket launched!")

        assert False, self._state

        return Op.STOP, None


def now():
    return time.time()

def run():
    work = [(0, Launch(d, c)) for d, c in rockets ]


if __name__ == "__main__":
    # for d, c in rockets():
    #     launch_rockets(d, c)
    # run_threads()
