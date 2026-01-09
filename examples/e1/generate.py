import os

with open("input.txt", "r") as f:
    outputs = f.readlines()

for o in outputs:
    open(o, "w")

print("Successfully Created the outputs for the inputs")