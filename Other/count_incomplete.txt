#!/bin/bash

grep -m 1 -v "Simulation finished" ./System_0/*.data >> incomplete.txt
