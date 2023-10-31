#!/bin/bash
 
file=$1
gcc -std=c99 -Wall -Werror -g "$file" -o app.exe -lm
