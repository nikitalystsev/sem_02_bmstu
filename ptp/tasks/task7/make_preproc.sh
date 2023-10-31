#!/bin/bash

array_sizes=("5" "500" "1000" "1500" "2000" "2500" "3000" "3500" "4000" "4500" "5000" "5500" "6000" "6500" "7000" "7500" "8000" "8500" "9000" "9500" "10000")
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
            ./apps/app3_"${size}"_"${opt}".exe >> ./data/data3_"${size}"_"${opt}".txt 

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
all_count=$((3 * len_array_sizes * len_opts))

echo -e "\nstart get info for graph1!"

for opt in "${opts[@]}"; do 
    for size in "${array_sizes[@]}"; do      
        for file in $files; do

            cd preproc_scripts/ || exit
            bash build_c_scripts.sh "one"
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
            if [ "${file}" == "data3_""${size}""_""${opt}"".txt" ]; then
                ar_time=$(preproc_scripts/ar_mean.exe < ./data/"${file}")
                echo "${size} ${ar_time}" >> ./postproc_data/grap1/data3_"${opt}".txt
                counter=$((counter + 1))
            fi

            echo -n -e "$counter/$all_count records were received\r"
        done
    done
done


echo  -e "\nfinish get info for graph1!"

#################################################################################################################

# первичный анализ и подготовка данных для построения второго графика

if ! [ -d ./postproc_data/grap2 ]; then
    mkdir postproc_data/grap2
fi

counter=0
all_count=$((3 * len_array_sizes))

echo -e "\nstart get info for graph2!"

for size in "${array_sizes[@]}"; do
    for file in $files; do

        cd preproc_scripts/ || exit
        bash build_c_scripts.sh "two" 
        cd ../

        if [ "$file" == "data_""${size}""_O2.txt" ]; then

            ar_time=$(preproc_scripts/ar_mean.exe < ./data/"$file")
            max=$(preproc_scripts/maximum.exe < ./data/"$file")
            min=$(preproc_scripts/minimum.exe < ./data/"$file")

            echo "${size} ${ar_time} ${min} ${max}" >> ./postproc_data/grap2/data_O2.txt
            counter=$((counter + 1))
        fi
        if [ "$file" == "data2_""${size}""_O2.txt" ]; then

            ar_time=$(preproc_scripts/ar_mean.exe < ./data/"$file")
            max=$(preproc_scripts/maximum.exe < ./data/"$file")
            min=$(preproc_scripts/minimum.exe < ./data/"$file")

            echo "${size} ${ar_time} ${min} ${max}" >> ./postproc_data/grap2/data2_O2.txt
            counter=$((counter + 1))
        fi

        if [ "$file" == "data3_""${size}""_O2.txt" ]; then

            ar_time=$(preproc_scripts/ar_mean.exe < ./data/"$file")
            max=$(preproc_scripts/maximum.exe < ./data/"$file")
            min=$(preproc_scripts/minimum.exe < ./data/"$file")

            echo "${size} ${ar_time} ${min} ${max}" >> ./postproc_data/grap2/data3_O2.txt
            counter=$((counter + 1))
        fi

        echo -n -e "$counter/$all_count records were received\r"
    done
done

echo  -e "\nfinish get info for graph2!"

#################################################################################################################

# первичный анализ и подготовка данных для построения третьего графика

if ! [ -d ./postproc_data/grap3 ]; then
    mkdir postproc_data/grap3
fi

counter=0
all_count="$len_array_sizes"

echo -e "\nstart get info for graph3!"

for size in "${array_sizes[@]}"; do
    for file in $files; do

        size_file=$(wc -l < ./data/"$file")
        cd preproc_scripts/ || exit
        bash build_c_scripts.sh "all" "$size_file"
        cd ../

        if [ "$file" == "data_""${size}""_O3.txt" ]; then

            ar_time=$(preproc_scripts/ar_mean.exe < ./data/"$file")
            max=$(preproc_scripts/maximum.exe < ./data/"$file")
            min=$(preproc_scripts/minimum.exe < ./data/"$file")
            median=$(preproc_scripts/median.exe < ./data/"$file")
            lower_quartile=$(preproc_scripts/lower_quartile.exe < ./data/"$file")
            upper_quartile=$(preproc_scripts/upper_quartile.exe < ./data/"$file")

            echo "${size} ${ar_time} ${min} ${lower_quartile}  ${median} ${upper_quartile} ${max}" >> ./postproc_data/grap3/data_O3.txt
            counter=$((counter + 1))
        fi  

        echo -n -e "$counter/$all_count records were received\r"   
    done
done
echo  -e "\nfinish get info for graph3!"

#################################################################################################################