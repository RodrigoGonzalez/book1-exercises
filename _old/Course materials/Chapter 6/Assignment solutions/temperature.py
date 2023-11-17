# 6.2 temperature.py
# Convert Celsius and Fahrenheit temperatures using functions

from __future__ import division


def convert_cel_to_far(cel_temp):
    return cel_temp * 9/5 + 32


def convert_far_to_cel(far_temp):
    return (far_temp - 32) * 5/9

temp1 = 72
print "{} degrees F = {} degrees C".format(temp1, convert_far_to_cel(temp1))

temp2 = 37
print "{} degrees C = {} degrees F".format(temp2, convert_cel_to_far(temp2))
