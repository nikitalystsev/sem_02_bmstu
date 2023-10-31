#!/bin/bash

array_sizes=("100" "200" "300" "400" "500" "600" "700" "800" "900" "1000")
opts=("Os" "O0" "O1" "O2" "O3")
count=10

################################################################################################################

# сборка основного датасета

len_array_sizes=${#array_sizes[@]}
len_opts=${#opts[@]}

counter=0 # счетчик
all_count=$((len_array_sizes * len_opts * 3 * count)) # общее количество возможных вариантов программ

# компилирую 
bash build_apps.sh



echo -e "\nstart collecting data!"

for c in $(seq "$count"); do
    for opt in "${opts[@]}"; do
        for size in "${array_sizes[@]}"; do
            # запускаю тестирование вот тут, 
            # count отвечает за количество строчек в файле ./data/data"${number}"_"${array_size}"_"${opt}".txt
            ./apps/app_"${size}"_"${opt}".exe >> ./data/data_"${size}"_"${opt}".txt 
            ./apps/app2_"${size}"_"${opt}".exe >> ./data/data2_"${size}"_"${opt}".txt 

            counter=$((counter + 3))
            echo -n -e "was collecting $counter/$all_count.  $c/$count $opt $size \r"
        done
    done
done

echo  -e "\nfinish collecting data!"

################################################################################################################

# проверка на то, есть ли в датасете добавленные записи, и если они есть, то отсутствующие размерности дописываются в массив

ls ./data > ls_data.txt
files_array=()
while IFS=" " read -r line; do files_array+=("$line"); done < <(grep -v "clean.sh" ls_data.txt)
rm ls_data.txt

for file in "${files_array[@]}"; do
    size=$(./find_size.sh "${file}")
    count=0
    for item in "${array_sizes[@]}"; do
        if [[ "$size" == "$item" ]]; then
            count=$((count + 1))
        fi
    done
    if [ "$count" -eq 0 ]; then
        array_sizes+=( "$size" )
    fi
done

len_array_sizes=${#array_sizes[@]}
len_opts=${#opts[@]}

#################################################################################################################

# первичный анализ и подготовка данных для построения первого графика

ls ./data > ls_data.txt
files=$(grep -v "clean.sh" ls_data.txt)
rm ls_data.txt


if ! [ -d ./postproc_data ]; then
    mkdir postproc_data
fi

if ! [ -d ./postproc_data/grap1 ]; then
    mkdir postproc_data/grap1
fi

counter=0
all_count=$((2 * len_array_sizes * len_opts))

echo -e "\nstart get info for graph1!"

for opt in "${opts[@]}"; do 
    for size in "${array_sizes[@]}"; do      
        for file in $files; do

            cd preproc_scripts/ || exit
            bash build_c_scripts.sh 
            cd ../

            if [ "${file}" == "data_""${size}""_""${opt}"".txt" ]; then
                ar_time=$(preproc_scripts/ar_mean.exe < ./data/"${file}")
                echo "${size} ${ar_time}" >> ./postproc_data/grap1/data_"${opt}".txt
                counter=$((counter + 1))
            fi
            if [ "${file}" == "data2_""${size}""_""${opt}"".txt" ]; then
                ar_time=$(preproc_scripts/ar_mean.exe < ./data/"${file}")
                echo "${size} ${ar_time}" >> ./postproc_data/grap1/data2_"${opt}".txt
                counter=$((counter + 1))
            fi

            echo -n -e "$counter/$all_count records were received\r"
        done
    done
done


echo  -e "\nfinish get info for graph1!"

# #################################################################################################################