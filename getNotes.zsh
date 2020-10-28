#!/bin/zsh

python copyNotes.py
chown -R jakebailey:staff content/
chmod -R 775 content/
