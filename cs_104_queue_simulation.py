# -*- coding: utf-8 -*-
"""CS 104 Queue Simulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vv57n1Ys0mPAL4FqpQPIRsv0JJJpT22Y
"""

# Alexander Metz
# Professor Eckert
# CS 104
# Fall 2023

names = []

for i in range(10):
  new_name = input("Enter name: ")
  names.append(new_name)

print(names)

for i in range(10):
  print(names.pop(0))

print(names)