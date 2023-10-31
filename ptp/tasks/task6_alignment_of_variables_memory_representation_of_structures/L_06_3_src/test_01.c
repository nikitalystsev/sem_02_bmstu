#include <stdio.h>


struct wnd_flags
{
    unsigned char show  : 1;
    unsigned char style : 2;
    unsigned char color : 3;
};


struct window
{
    // другие обычные поля

    struct wnd_flags flags;
};


int main(void)
{
    struct window w;
    unsigned char f;

    // error: incompatible types when assigning to type 'struct wnd_flags' from type 'int'
    w.flags = 5;

    // error: incompatible types when assigning to type 'unsigned char' from type 'struct wnd_flags'
    f = w.flags;

    (void) w;
    (void) f;

    return 0;
}