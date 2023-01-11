import os
import sys

args = sys.argv
root_dir = "."

if len(args) < 2:
    print("Directory is not specified")
else:
    root_dir = args[1]


for root, dirs, files in os.walk(root_dir, topdown=True):
    for name in files:
        print(os.path.join(root, name))
