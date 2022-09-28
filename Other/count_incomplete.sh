#!/bin/bash

grep -m 1 -L "Simulation finished" ./System_0/*.data >> incomplete.txt
