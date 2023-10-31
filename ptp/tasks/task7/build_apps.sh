#!/bin/bash

array_sizes=("5" "500" "1000" "1500" "2000" "2500" "3000" "3500" "4000" "4500" "5000" "5500" "6000" "6500" "7000" "7500" "8000" "8500" "9000" "9500" "10000")
opts=("Os" "O0" "O1" "O2" "O3")

len_array_sizes=${#array_sizes[@]}
len_opts=${#opts[@]}

count=0
all_count=$((len_array_sizes * len_opts * 3))

if ! [ -d ./apps ]; then
    mkdir apps
fi

echo "start compiling!"

for size in "${array_sizes[@]}"; do
    for opt in "${opts[@]}"; do
        gcc -std=c99 -Wall -Werror -Wpedantic -DNMAX="${size}"\
        -Wextra -Wfloat-conversion -Wfloat-equal -"${opt}" \
        -Wvla -o ./apps/app_"${size}"_"${opt}".exe main.c 

        gcc -std=c99 -Wall -Werror -Wpedantic -DNMAX="${size}"\
        -Wextra -Wfloat-conversion -Wfloat-equal -"${opt}" \
        -Wvla -o ./apps/app2_"${size}"_"${opt}".exe main2.c 

        gcc -std=c99 -Wall -Werror -Wpedantic -DNMAX="${size}"\
        -Wextra -Wfloat-conversion -Wfloat-equal -"${opt}" \
        -Wvla -o ./apps/app3_"${size}"_"${opt}".exe main3.c 
        count=$((count + 3))
        echo -n -e "was compiling $count/$all_count files\r"
    done
done

echo -e "\nfinish compiling!"
