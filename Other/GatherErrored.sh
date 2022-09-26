#!/bin/bash

grep "WARNING: INAPPROPRIATE NUMBER OF UNIT CELLS USED" ./System_0/*.data >> Errored.txt
