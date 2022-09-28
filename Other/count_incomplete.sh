#!/bin/bash

echo "" > incomplete.txt
grep -m 1 -L "Simulation finished" ./System_0/*.data >> incomplete.txt
