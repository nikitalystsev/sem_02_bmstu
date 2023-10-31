#!/bin/bash

gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -g3 -pg -c main.c
gcc -pg -o app.exe main.o -lm

gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -g3 - -c main2.c
gcc -o app2.exe main2.o -lm

