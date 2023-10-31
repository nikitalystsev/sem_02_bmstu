#!/bin/bash

./sq.exe < in_1.txt > out.txt

if diff out.txt out_1.txt; then
  echo TEST1: pass
else
  echo TEST1: fail
fi

./sq.exe < in_2.txt > out.txt

if diff out.txt out_2.txt; then
  echo TEST2: pass
else
  echo TEST2: fail
fi
