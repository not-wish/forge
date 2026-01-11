import os

with open("input.txt", "r") as f:
    outputs = f.readlines()

for o in outputs:
    open(o.strip("\n"), "w")

print("Successfully Created the outputs for the inputs")