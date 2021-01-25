## My script to move my notes into the content folder
## Recursively filtered (and sorted?) and flat structure

import os
import shutil
import sys

if len(sys.argv) == 1:
    switch = True
else:
    if sys.argv[1] == "-w":
        switch = True
    else:
        switch = False

if switch:
    # We're on windows
    sourceDirectory = "C:/Users/asaxp/OneDrive/Org/Slipbox"
    destinationDirectory = "C:/Users/asaxp/OneDrive/Workspace/notesSite/content"
else:
    # We're on Mac
    sourceDirectory = "/Users/jakebailey/OneDrive/Org/Slipbox"
    destinationDirectory = "/Users/jakebailey/OneDrive/Workspace/notesSite/content"


## Clean destination
for root, dires, files in os.walk(destinationDirectory):
    for f in files:
        os.remove(os.path.join(root, f))

for root, dirs, files in os.walk(sourceDirectory):
    for f in files:
        if f.endswith(".md"):
            shutil.copy2(os.path.join(root,f), os.path.join(destinationDirectory, f))
