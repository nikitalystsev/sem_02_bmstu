#!/bin/bash

if [ "$1" == "one" ]; then
    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o ar_mean.exe ar_mean.c -lm
fi

if [ "$1" == "two" ]; then
    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o ar_mean.exe ar_mean.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o maximum.exe maximum.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o minimum.exe minimum.c -lm
fi

if [ "$1" == "all" ]; then
    size="$2"
    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o ar_mean.exe ar_mean.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -DN="${size}" -Wvla -o lower_quartile.exe lower_quartile.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o maximum.exe maximum.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -DN="${size}" -Wvla -o median.exe median.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -Wvla -o minimum.exe minimum.c -lm

    gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal -DN="${size}" -Wvla -o upper_quartile.exe upper_quartile.c -lm
fi

