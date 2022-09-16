#!/bin/bash

echo $(qstat) > tasks.txt

echo $(python3 parseTasks.py)

