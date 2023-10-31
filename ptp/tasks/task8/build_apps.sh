#!/bin/bash

array_sizes=("100" "200" "300" "400" "500" "600" "700" "800" "900" "1000")
opts=("Os" "O0" "O1" "O2" "O3")

len_array_sizes=${#array_sizes[@]}
len_opts=${#opts[@]}

count=0
all_count=$((len_array_sizes * len_opts * 2))

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
        
        count=$((count + 2))
        echo -n -e "was compiling $count/$all_count files\r"
    done
done

echo -e "\nfinish compiling!"
