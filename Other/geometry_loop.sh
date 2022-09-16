#!/bin/bash

for cif in *.cif; do
	./network -volpo 1.5 1.5 50000 ${cif}
	./network -sa 1.5 1.5 2000 ${cif}
	./network -res ${cif%.cif}_output.res ${cif}
done

cat *.res > OUTPUT_res.txt
cat *.sa > OUTPUT_sa.txt
cat *.volpo > OUTPUT_volpo.txt
