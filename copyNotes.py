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

if len(sys.argv) > 2:
    ## We've been passed source
    if len(sys.argv) < 4:
        ## But not dest. Error
        print("If specifying source, you must also specify dest.")
        exit(-1)
    
    sourceDirectory = str(sys.argv[2])
    destinationDirectory = str(sys.argv[3])

## Clean destination
for root, dirs, files in os.walk(destinationDirectory):
    for f in files:
        os.remove(os.path.join(root, f))

excl_dirs = {'../build', 'build', 'build/content'}

for root, dirs, files in os.walk(sourceDirectory):
    dirs[:] = [d for d in dirs if d not in excl_dirs]
    for f in files:
        if f.endswith(".md"):
            print(f)
            shutil.copy2(os.path.join(root,f), os.path.join(destinationDirectory, f))
