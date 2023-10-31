/*
Слайд 25
*/

#include <stdio.h>


int main(void)
{
    union word
    {
        unsigned short word;
        // для little endian
        struct word_parts
        {
            // младший байт
            unsigned char lo;
            // старший байт
            unsigned char hi;
        } parts;
    } a;

    a.word = 0xABCD;

    printf("word 0x%4x, hi part 0x%2x, lo part 0x%2x",
                           a.word, a.parts.hi, a.parts.lo);

    return 0;
}