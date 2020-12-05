#!/usr/bin/env python
# -*- coding: utf-8 -*-

import machine

class Servo:

    def __init__(self, pin, freq=100, pos=50):
        self.freq = freq
        self.T = 1000000 / freq  # period in us
        t = 1000 + pos * 10 # 1000 - 2000 us
        if t < 1000:
            t = 1000
        if t > 2000:
            t = 2000
        duty = int(t / self.T * 1023)
        self.pwm = machine.PWM(machine.Pin(pin), freq=100, duty=duty)

    def set(self, pos):
        t = 1000 + pos * 10 # 1000 - 2000 us
        if t < 1000:
            t = 1000
        if t > 2000:
            t = 2000
        duty = int(t / self.T * 1023)
        self.pwm.duty(duty)

    def off(self):
        self.deinit()

    def on(self):
        self.__init__(self, self.pin)


