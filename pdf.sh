#!/bin/bash
echo " *: CONVERTING JPEG FILES INTO PDF for "$1" many JPGs"
F=""
for s in $(seq 0 $1); do 
  F=$F" cap/"$s".jpg"
done
echo $F
img2pdf $F --output cap/out.pdf
