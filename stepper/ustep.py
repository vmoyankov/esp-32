#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import *

from time import sleep
import random

class Stepper():
    def __init__(self, a1, a2, b1, b2):
        self.a1 = Pin(a1, mode=Pin.OUT, value=0)
        self.a2 = Pin(a2, mode=Pin.OUT, value=0)
        self.b1 = Pin(b1, mode=Pin.OUT, value=0)
        self.b2 = Pin(b2, mode=Pin.OUT, value=0)

        self.pos = 0

    def _set(self):
        a, b = [
                (1, 1),
                (0, 1),
                (0, 0),
                (1, 0)] [self.pos % 4]
        self.a1.value(a)
        self.a2.value(1-a)
        self.b1.value(b)
        self.b2.value(1-b)

    def step(self, dir):
        self.pos = (self.pos + dir) % 4
        self._set()

    def deinit(self):
        self.a1.mode(Pin.IN)
        self.a2.mode(Pin.IN)
        self.b1.mode(Pin.IN)
        self.b2.mode(Pin.IN)


def main():
    a1, a2, b1, b2 = (15, 2, 4, 5)
    s = Stepper(a1, a2, b1, b2)
    
    try:
        while True:
            tm = 1.0 / random.randint(40,150)
            for i in range(random.randint(10,40)):
                s.step(-1)
                sleep(tm)
            tm = 1.0 / random.randint(40,150)
            for i in range(random.randint(5,30)):
                s.step(1)
                sleep(tm)
    except:
        s.deinit()
        raise

if __name__ == '__main__':
    main()
