## My script to move my notes into the content folder
## Recursively filtered (and sorted?) and flat structure

import os
import shutil

sourceDirectory = "/Volumes/Anonymous/OneDrive/Org/Slipbox"
destinationDirectory = "/Users/jakebailey/Projects/NotesSite/content"

## Clean destination
for root, dires, files in os.walk(destinationDirectory):
    for f in files:
        os.remove(os.path.join(root, f))

for root, dirs, files in os.walk(sourceDirectory):
    for f in files:
        if f.endswith(".md"):
           shutil.copy2(os.path.join(root,f), os.path.join(destinationDirectory, f))
