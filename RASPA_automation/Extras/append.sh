#!/bin/bash
input="Structures_current.txt"
while IFS= read -r line
do
  echo "$line" >> "Structures.txt"
  echo "$line"
done < "$input"
