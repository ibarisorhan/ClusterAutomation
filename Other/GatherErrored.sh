#!/bin/bash

grep -m 1 "WARNING: INAPPROPRIATE NUMBER OF UNIT CELLS USED" ./System_0/*.data >> Errored.txt
