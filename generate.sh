#!/bin/bash
python3 readreddit.py -r "$1" -v $2
python3 createaudio.py 
